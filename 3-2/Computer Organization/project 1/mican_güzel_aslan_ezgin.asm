.data
	mainstring: .asciiz "\nWelcome to our MIPS project!\nMain Menu:\n1. Base Converter\n2. Add Rational Number\n3. Text Parser\n4. Mystery Matrix Operation\n5. Exit\nPlease select an option:"
	
	############# rational numbers data
	firstn: .asciiz "Enter the first numerator: "
	firstd: .asciiz "Enter the first denominator: "
	secondn: .asciiz "Enter the second numerator: "
	secondd: .asciiz "Enter the second denominator: "
	delimeter1: .asciiz "/"
	delimeter2: .asciiz "+"
	delimeter3: .asciiz "="
	####################################
	
	#################### base converter data
	
	prompt: .asciiz "Input: "
	prompt1: .asciiz "Type: "
	fileInputBuffer: .space 80
	binaryinput: .space 50
	
	####################################
	
	#################### text parser data
	txtprsrmsg: .asciiz "\nInput text: "
	txtprsrs: .asciiz "Parser characters: "
	newlinestr: .asciiz "\n"
	txt: .space 120
	parsers: .space 20
	####################################
	
	#################### mystery matrix operation data
	
	
	
	####################################
.text
	UI: # User Interface
		li $v0, 4 #UI
		la $a0, mainstring
		syscall
		
		li $v0, 5 #input
		syscall
		
		beq $v0, 5, exit #options
		beq $v0, 4, matrixop
		beq $v0, 3, textparser
		beq $v0, 2, rationalnumber
		beq $v0, 1, baseconverter
		
		j UI #loop
	
	#########################################
	baseconverter: # base converter func start
	
		# Prompt the user to enter input
     		li $v0, 4
     		la $a0, prompt
     		syscall
     
     		li $v0, 8
     		la $a0, binaryinput
		li $a1, 50
     		syscall
  
     		#Transfer the input $t0 for modifeing
     		la $t0, binaryinput
     
     		#Prompt the user to enter type
     		li $v0, 4
		la $a0, prompt1
     		syscall
     
     		li $v0, 5 #input
     		syscall
     
     		beq $v0, 1, readBits #options

	readBits:   #Function to read bits
     		add $t5, $t0, $zero     #set t5 to parameter
     		li $t1, 2             #base value (2)
     		li $t7 , 0            #j = 0
     		li $s0, 0             # Set return value to 0
     		li $s7, '0'           # load ascii value of '0'
     
     		j readBitsLoop
	readBitsLoop:
     		beq $t7, $t5, endReadBitsLoop   #If we are past our length's iteration, we have rs
     		lb $t2, 0($t0)    #Load in byte in file
     		addi $t0, $t0, 3       # iterator for file++
     		addi $t7, $t7, 1       # j++
     		mult $s0, $t1          #multiply return value and base
     		mflo $t3              #set result to t5
     		sub $t4, $t2, $s7   #subtract fileInputBuffer[i] and ascii value for '0'
     		add $s0, $t3,$t4        #Add those 2 together
     
     		li $v0, 1
     		move $a0, $t2
     		syscall

     		j endReadBitsLoop     #Jump to start of loop
	endReadBitsLoop:
     		add $v0, $s0, $zero #move return value to return register
   	
   		j UI
	##############################################
	rationalnumber: # rational number func start
		li $v0, 4
		la $a0, firstn
		syscall
		
		li $v0, 5
		syscall
		
		move $t0, $v0 #first numerator
		
		li $v0, 4
		la $a0, firstd
		syscall
		
		li $v0, 5
		syscall
		
		move $t1, $v0 #first denominator
		
		li $v0, 4
		la $a0, secondn
		syscall
		
		li $v0, 5
		syscall
		
		move $t2, $v0 #second numerator
		
		li $v0, 4
		la $a0, secondd
		syscall
		
		li $v0, 5
		syscall
		
		move $t3, $v0 #second denominator
		
		li $v0, 1 #print first num
		move $a0, $t0
		syscall
		
		li $v0, 4
		la $a0, delimeter1
		syscall
		
		li $v0, 1 #print second num
		move $a0, $t1
		syscall
		
		li $v0, 4
		la $a0, delimeter2
		syscall
		
		li $v0, 1 #print third num
		move $a0, $t2
		syscall
		
		li $v0, 4
		la $a0, delimeter1
		syscall
		
		li $v0, 1 #print last num
		move $a0, $t3
		syscall
		
		li $v0, 4
		la $a0, delimeter3
		syscall
		
		mul $t0, $t0, $t3 #first numerator multiplied
		mul $t2, $t2, $t1 #second numerator multiplied
		
		mul $t1, $t1, $t3 #firs denominator multiplied
		
		add $t0, $t0, $t2 #numerator
		
		move $a0, $t0 #numerator
		move $a1, $t1 #denominator
		
		jal GCD #GCD function call
		
		
	GCD: #GCD of $t3 and $t1
		addi $sp, $sp, -12
		
		sw $ra, 0($sp)
		sw $s0, 4($sp)
		sw $s1, 8($sp)
		
		add $s0, $a0, $zero #t1 value
		add $s1, $a1, $zero #t3 value
		
		addi $t9, $zero, 0
		beq $s1, $t9, returnnumber
		
		add $a0, $zero, $s1
		div $s0, $s1
		mfhi $a1
		
		jal GCD
	
	returnnumber:
		add $v0, $zero, $s0
		add $t4, $v0, $zero
		
		div $s0, $t1, $t4 #s0 is the simplified denominator
		div $s1, $t0, $t4 #s1 is the simplified numerator
		
		add $s5, $zero, $s0 #new denominator
		add $s6, $zero, $s1 #new numerator
		
		li $v0, 1
		move $a0, $s1
		syscall
		
		li $v0, 4
		la $a0, delimeter1
		syscall
		
		li $v0, 1
		move $a0, $s0
		syscall
		
		j UI
	#################################################################
	
	textparser: # text parser func start
		la $a0, txtprsrmsg
		li $v0, 4	 #input string
		syscall
		
		li $v0, 8
		la $a0, txt
		li $a1, 100
		syscall
		
		la $a0, txtprsrs
		li $v0, 4	#input parser characters
		syscall
		
		li $v0, 8
		la $a0, parsers
		li $a1, 20
		syscall
		
		la $t0, txt
		la $t1, parsers
		li $a3, 0x20 #space
	
	printerLoop: #prints words
		lb $t2, 0($t0)
		
		beqz $t2, UI
		
		j searcherLoop
		
	searcherLoop: #searching in parsers
		lb $t3, 0($t1)
		
		beq $t2, $t3, newLine #if equal, print new line
		beq $t2, $a3, newLine #if space, print new line
		beqz $t3, print #if parser list is finished, print the character
		
		addi $t1, $t1, 1
		j searcherLoop
	newLine:
		la $a0, newlinestr
		li $v0, 4	 #new line
		syscall
		addi $t0, $t0, 1
		la $t1, parsers
		j printerLoop
	print:
		la $a0, ($t2)
		li $v0, 11	 #print char
		syscall
		addi $t0, $t0, 1
		la $t1, parsers
		j printerLoop
	#################################################################
	
	matrixop: # mystery matrix operation func start
		
	exit: # exit func start
		li $v0, 10 #stops the program
		syscall
