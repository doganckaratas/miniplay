#define _GNU_SOURCE
#ifndef _SOCKET_H
#define _SOCKET_H

int socket_resolve_host(const char *, char **);
int socket_connect(int *, const char *, int );
int socket_open(int *);
int socket_close(int *);
int socket_get_api();

#endif /* _SOCKET_H */
