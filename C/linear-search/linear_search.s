	.file	"main.c"
	.section	.rodata
.LC0:
	.string	"Value not found."
.LC1:
	.string	"Found value in place %lu.\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$64, %rsp
	movl	$1, -64(%rbp)
	movl	$2, -60(%rbp)
	movl	$3, -56(%rbp)
	movl	$4, -52(%rbp)
	movl	$5, -48(%rbp)
	movl	$6, -44(%rbp)
	movl	$7, -40(%rbp)
	movl	$8, -36(%rbp)
	movl	$9, -32(%rbp)
	movl	$5, -28(%rbp)
	movl	$5, -12(%rbp)
	movq	$0, -8(%rbp)
	jmp	.L2
.L5:
	movq	-8(%rbp), %rax
	addq	$1, %rax
	movl	-64(%rbp,%rax,4), %eax
	cmpl	-12(%rbp), %eax
	jne	.L3
	addq	$1, -8(%rbp)
	jmp	.L4
.L3:
	addq	$2, -8(%rbp)
.L2:
	movq	-8(%rbp), %rax
	movl	-64(%rbp,%rax,4), %eax
	cmpl	-12(%rbp), %eax
	jne	.L5
.L4:
	cmpq	$9, -8(%rbp)
	jne	.L6
	leaq	.LC0(%rip), %rdi
	call	puts@PLT
	movl	$1, %eax
	jmp	.L8
.L6:
	movq	-8(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC1(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
.L8:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Debian 6.3.0-18+deb9u1) 6.3.0 20170516"
	.section	.note.GNU-stack,"",@progbits
