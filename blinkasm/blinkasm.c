#include <stdio.h>
#include "pico/stdlib.h"

void run_asm();

void gpio_put_wrapper(int pin, int val)
{
	gpio_put(pin, val);
}
void sleep_ms_wrapper(int ms)
{
	sleep_ms(ms);
}

int main()
{
	gpio_init(25);
	gpio_set_dir(25, GPIO_OUT);
	sleep_ms(1000);

	run_asm();
}
