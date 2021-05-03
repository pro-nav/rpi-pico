.global run_asm

run_asm:
	ldr r0, =#25
	ldr r1, =#0
	bl gpio_put_wrapper

	ldr r0, =#250
	bl sleep_ms_wrapper

	ldr r0, =#25
	ldr r1, =#1
	bl gpio_put_wrapper

	ldr r0, =#250
	bl sleep_ms_wrapper

	bl run_asm
