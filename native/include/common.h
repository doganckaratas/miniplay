#ifndef _COMMON_H
#define _COMMON_H

#define VER "0.1b"

enum log_level_e {
	LOG_ERROR,
	LOG_DEBUG,
	LOG_INFO,
	LOG_TRACE
};

#define NORM	"\33[0m"
#define GRAY	"\33[30m"
#define RED	"\33[31m"
#define GREEN	"\33[32m"
#define YELLOW	"\33[33m"
#define BLUE	"\33[34m"
#define PURPLE	"\33[35m"
#define CYAN	"\33[36m"
#define DWHITE	"\33[37;1m"
#define DGRAY	"\33[30;1m"
#define DRED	"\33[31;1m"
#define DGREEN	"\33[32;1m"
#define DYELLOW	"\33[33;1m"
#define DBLUE	"\33[34;1m"
#define DPURPLE	"\33[35;1m"
#define DCYAN	"\33[36;1m"
#define DWHITE	"\33[37;1m"

typedef struct {
	enum log_level_e level;
	void (*log_t)(const char *fmt, ...);
	void (*log_i)(const char *fmt, ...);
	void (*log_d)(const char *fmt, ...);
	void (*log_e)(const char *fmt, ...);
} Logger;
Logger *logger;

/* Public Functions */
void logger_init(Logger **logger);
void logger_set_level(Logger *logger, enum log_level_e lvl);
void logger_destroy(Logger **logger);

#endif /* _COMMON_H */
