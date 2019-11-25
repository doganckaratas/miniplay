#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

#include "common.h"

/* Private Functions */
static void logger_debug(const char *fmt, ...)
{
	va_list args;
	va_start(args, fmt);
	printf(DGREEN"[DEBUG]"NORM" ");
	vprintf(fmt, args);
	va_end(args);
	return;
}

static void logger_error(const char *fmt, ...)
{
	va_list args;
	va_start(args, fmt);
	printf(DRED"[ERROR]"NORM" ");
	vprintf(fmt, args);
	va_end(args);
	return;
}

static void logger_info(const char *fmt, ...)
{
	va_list args;
	va_start(args, fmt);
	printf(DYELLOW"[INFO ]"NORM" ");
	vprintf(fmt, args);
	va_end(args);
	return;
}

static void logger_null(const char *fmt, ...)
{
	(void) fmt;
	return;
}

/* Public Functions */
void logger_init(Logger **logger)
{
	*logger = (Logger *) malloc(sizeof(Logger));
}

void logger_set_level(Logger *logger, enum log_level_e lvl)
{
	if (!logger) {
		return;
	}

	logger->level = lvl;

	switch (logger->level) {
		case LOG_DBG:
			logger->log_i = &logger_info;
			logger->log_d = &logger_debug;
			logger->log_e = &logger_error;

		break;
		case LOG_INF:
			logger->log_i = &logger_info;
			logger->log_d = &logger_null;
			logger->log_e = &logger_error;

		break;
		case LOG_ERR:
			logger->log_i = &logger_null;
			logger->log_d = &logger_null;
			logger->log_e = &logger_error;

		break;
		default:
			logger->log_i = &logger_null;
			logger->log_d = &logger_null;
			logger->log_e = &logger_null;

		break;
	}
}

void logger_destroy(Logger **logger)
{
	if (*logger) {
		free(*logger);
		*logger = NULL;
	}
}
