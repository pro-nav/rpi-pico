#include "pico/stdlib.h"

#define HIGH 1
#define LOW 0

#define LED 25

int main()
{
    gpio_init(LED);
    gpio_set_dir(LED, GPIO_OUT);

    while (1)
    {
        gpio_put(LED, HIGH);
        sleep_ms(1000);
        gpio_put(LED, LOW);
        sleep_ms(1000);
    }
}