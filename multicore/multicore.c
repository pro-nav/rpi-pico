#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/multicore.h"

#define LOW 0
#define HIGH 1
#define LED 25

void core1_part()
{
	while(1){
		gpio_put(LED, HIGH);
		sleep_ms(700);
		gpio_put(LED, LOW);
		sleep_ms(700);
	}
}

int main()
{
	gpio_init(LED);
	gpio_set_dir(LED, GPIO_OUT);

	multicore_launch_core1(core1_part);

	while (1)
	{
		gpio_put(LED, HIGH);
		sleep_ms(2000);
		gpio_put(LED, LOW);
		sleep_ms(2000);	
	}
}
