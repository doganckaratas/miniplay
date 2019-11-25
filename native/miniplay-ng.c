#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "common.h"
#include "socket.h"

int main(int argc, char **argv)
{
	/* Terminal Setup */
	logger_init(&logger);
	logger_set_level(logger, LOG_DBG);
	logger->log_i("miniplay-ng "VER" \n");
	socket_get_api();
	logger_destroy(&logger);
	return 0;
}
