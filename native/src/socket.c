#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdarg.h>
#include <assert.h>

#include <netdb.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <errno.h>
extern int h_errno;

#include "common.h"
#include "socket.h"

int socket_resolve_host(const char *hostname, char **ip)
{
	struct hostent *h;
	struct in_addr **in_addr_list;
	int i;

	h = gethostbyname(hostname);
	if (h == NULL) {
		logger->log_e("%s: %s\n", hstrerror(h_errno), hostname);
		return -1;
	}

	in_addr_list = (struct in_addr **) h->h_addr_list;
	for(i = 0; in_addr_list[i] != NULL; i++) {
		break;
	}

	asprintf(ip, "%s", inet_ntoa(*in_addr_list[i]));
	return 0;
}

int socket_connect(int *fd, const char *remote_ip, int port)
{
	struct sockaddr_in server;

	server.sin_addr.s_addr = inet_addr(remote_ip);
	server.sin_family = AF_INET;
	server.sin_port = htons(port);

	if (connect(*fd, (struct sockaddr *) &server, sizeof(server)) < 0) {
		logger->log_e("Could not connect to %s:%d failed with %d (%s) code.\n", remote_ip, port, errno, strerror(errno));
		return -1;
	}
	return 0;
}

int socket_get_api()
{
	char *api_host = "api.radyofenomen.com";
	char *api_key  = "/Channels/?appRef=FenomenWebV2";
	char *api_request = "GET %s HTTP/2.0\r\n"
				"Host: %s\r\n"
				"User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0\r\n"
				"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
				"Accept-Language: en-US,en;q=0.5\r\n"
				"Accept-Encoding: gzip, deflate, br\r\n"
				"DNT: 1\r\n"
				"Connection: keep-alive\r\n"
				"Content-Type: text/html\r\n"
				"Upgrade-Insecure-Requests: 1\r\n"
				"Pragma: no-cache\r\n"
				"Cache-Control: no-cache\r\n"
				"TE: Trailers\r\n\r\n";
	int sockfd = 0;
	char *ip = NULL;
	int port = 443;
	socket_open(&sockfd);
	socket_resolve_host(api_host, &ip);
	logger->log_d("Host: %s IP: %s\n", api_host, ip);
	logger->log_i("Connecting...\n");
	socket_connect(&sockfd, ip, port);
	char *request = NULL;
	char *response[65536] = {0};
	asprintf(&request, api_request, api_key, api_host);
	logger->log_d("Request: \n%s\n", request);
	logger->log_d("Bytes sent: %d\n",send(sockfd, request, strlen(request), 0));
	logger->log_d("Bytes received: %d\n",recv(sockfd, response, 65536, 0));
	logger->log_d("Response: %s\n", response);
	socket_close(&sockfd);
	free(ip);
	return 0;
}

int socket_open(int *fd)
{
	if (!fd) {
		return -1;
	}

	*fd = socket(AF_INET, SOCK_STREAM, 0);
	if (!fd) {
		logger->log_e("Socket could not be created. ");
		perror("");
		return -2;
	}
	return 0;
}

int socket_close(int *fd)
{
	if (!fd) {
		return -1;
	}

	return 0;
}
