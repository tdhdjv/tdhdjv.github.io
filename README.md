# SoME4nion

## Introduction
If you've worked on computer graphics, computer vision, robotics or something related to quaternions. It's likely that you have heard of **quaternions**. There are already a plethora amount of videos, and online resources, explaining **quaternions**. However many of these resources either focus only on the application, skipping over a lot of the math, or explain using algebra, which doesn't build an intuitive relation behind quaternions and 3D rotation. This blog is my attempt to explain **quaternions** in a mathematical way, building from the foundation and giving a geometric interpretation of **quaternions**.

## Real Numbers
When we think of numbers we usually think of numbers, numbers such as 1, 2, 3.14159265 seem to come to mind. We are familiar with these numbers as they are used all the time. These numbers are called real numbers(kind of a terrible name but whatever). When it comes to visualizing the real numbers, a common way of doing so is with a number line. The number line starts from 0 and as the values get bigger as you go right, and as it gets smaller you go left.  </br>

![CreateCircle_ManimCE_v0 19 0](https://github.com/user-attachments/assets/dea4eddb-8dcc-40f7-becd-13b40bf5a36c)

Every point on the line represents a single real number. This provides a way of associating geometry to the reals.

### Arthmetics on the Number Line

#### Addition/Subtraction
Numbers in it of itself are not interesting, instead operations and relationships between these numbers make them useful.
Addition is one of these operations. To think about addition in the number line we'll start by thinking about numbers in a different manner. As said earlier a number is a point in the number, and therefore we can draw an arrow starting from 0 and extend it to this point. This arrow will represent the number, the length will represent the value, and the direction will decide the sign. Now addition then can be thought up as connecting these to arrows.  </br>

![NumberLineArrow_ManimCE_v0 19 0](https://github.com/user-attachments/assets/531af2c3-46c6-4f3f-b2b8-3d4b268712e3)

Subtraction is the same as adding up a negative number, and since negative numbers are just arrows with the same length pointing backwards, subtraction is already defined.

#### Multiplication:
We can also visualize multiplication in plane. $`a{\cdot}b`$ can be thought up as arrow $`b`$ becoming $`a`$ times longer, if a is negative it can be thought up as reversing the direction of $`b`$ </br>

![Multiply_ManimCE_v0 19 0](https://github.com/user-attachments/assets/30a111c0-647e-44d4-9ca6-54541ffffee2)</br>

## Thinking about Multiple Numbers
We have worked with 1 number, now let’s see how we can think of 2 numbers(I will write a pair of numbers as $`(a, b)`$). When we visualized 1 number we used a line so for 2 numbers let's use 2 lines. The first number of our pair will be on the first line, and the second number of our pair will be the second line. To visualise these numbers into 1 space let's make the second line perpendicular to the first, and now we have a plane where every point can be represented. </br>

![CoordinatePlane_ManimCE_v0 19 0](https://github.com/user-attachments/assets/68edbf5c-b190-4199-94ac-880272dfcccf)

These pairs of numbers are referred to as vectors, more specifically 2 dimensional vectors, I will be calling them as vectors for the rest of this blog convenience sake.

### Vector Arithmetics
#### Addition
These vectors similar to real numbers can be added up. The definition of this addition is this $`(a,b)+(c,d)=(a+b,c+d)`$. now let's see if we can interpret this geometrically. As we did with real numbers, these vectors can be thought up as arrows pointing from the origin($`(0, 0)`$) to the point in the plane. So it follows that adding 2 vectors will also be the concatenation of these arrows. 

![VectorAddition_ManimCE_v0 19 0](https://github.com/user-attachments/assets/21ce5366-c6fb-4f9c-aae7-7f475f4ad5d2)

When we do this we can see that each of the horizontal components are added up, and each of the vertical components are also added up. Therefore it satisfies our definition of vector addition.

![VectorAdditionAgain_ManimCE_v0 19 0](https://github.com/user-attachments/assets/a9a1c9ae-3e74-4c88-b29a-04550d02718a)

#### Multiplication
Now there is no way to multiply 2 vector, or at least no one universial way. There is a [Freya Holmér Video](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DhtYh-Tq7ZBI&ved=2ahUKEwii-ZTwyL2OAxV1rlYBHd1eO1QQtwJ6BAgYEAI&usg=AOvVaw1Pof5zvOx6Em9U4nVKYis3) about this topic. However, we can multiply a vector with a real number. The defintion is $`a{\cdot}(b,c)=(a{\cdot}b,a{\cdot}c)`$. Geometrically we can think of this as taking the arrow $`(b,c)`$ and extending it $`a`$ times. 

![VectorMul_ManimCE_v0 19 0](https://github.com/user-attachments/assets/71bebf78-08ad-4fe7-8300-65766ef16e2e)

## The Definition of Imaginary Numbers
I would like you to imagine(pun unintended) an equation. $`x^2={-1}`$, with real numbers there is no x that satisfy this equation, as all real numbers squared are positive.</br>
However, let us make up a new number $`i`$, and say that $`i^2={-1}`$. With this definition of $`i`$ we can know 2 facts about it. 
1. $`i`$ is not real(as in numbers)
2. $`i^2={-1}`$

## Complex Numbers
Now that we define imaginary numbers and real numbers. Let's add them together. Let's say we have a number $`a`$, and $`b{i}`$. As mentioned, imaginary numbers aren’t real numbers therefore, imaginary numbers and real numbers can’t be reduced to a single new value. So instead we have to write them as $`a+b{i}`$ These numbers which are composed of real and imaginary numbers are called complex numbers. 

### Complex Arithmetic

#### Addition:
when adding up 2 complex numbers $`a+b{i}`$ with $`c+d{i}`$, we can see that the real, and the imaginary parts can be added together to get $`(a+c)+(b+d){i}`$. 

### Multiplication with real numbers
Multiplication of $`a{\cdot}(b+c{i})`$ is defined as $`a{\cdot}b+a{\cdot}c{i}`$.

### Conclusion:
As we can see the complex numbers mirror 2 dimensional vectors, addition, and multiplication with real numbers are the same. Therefore complex numbers can be mapped to a plane. Let's call this plane the complex plane.

### Complex Multiplication
A fact that differentiates complex numbers from vectors is multiplication. Vectors can't be multiplied by themselves, however there is one universal way to multiply 2 complex numbers. Complex number multiplication satisfies the properties of real number multiplication. That being
- associativity $`a{\cdot}(b{\cdot}c)=(a{\cdot}b){\cdot}c=a{\cdot}b{\cdot}c`$
- distributivity $`a{\cdot}(b+c)=a{\cdot}b+a{\cdot}c`$
- commutativity $`a{\cdot}b = b{\cdot}a`$

With these properties we can define complex number multiplications. $`(a+b{i}){\cdot}(c+d{i})=(a{\cdot}c-b{\cdot}d)+(b{\cdot}d+a{\cdot}c){i}`$ </br>

## Complex Numbers as Rotations:
There is a sense in which complex numbers can encode rotating in 2d spaces. there is a famous equation showing this $`e^{i{\pi}}={-1}`$. the general case being $`e^{{i}x}=cos{x}+{i}sin{t}`$. Although 3b1b has already made a [video](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3Dv0YEaeIClKY&ved=2ahUKEwiL9Kyjz72OAxVUrVYBHc3XNQ4QtwJ6BAgTEAI&usg=AOvVaw3mfbkRSaPOODDaVBFlPXZk) about this. However I will explain it here as this is crucial for the rest of the blog.</br>

### Times i is rotation
when a $`1`$ is multiplied by $`i`$ it becomes $`i`$, and when $`i`$ is multiplied by $`{i}`$ it $`-1`$ becomes we see that it rotates the number 90 degrees clockwise. 

[pic]

We can extend this to every complex number, as complex numbers are composed of $`1`$'s and $`i`$'s. </br>

[pic] </br>

### Deriving meaning from $`\mathbf{e^{x{i}}}`$
Now the important part, let’s think about the $`f(t)=e^{t{i}}`$. If we were to differentiate this function $`f'(t)=i{\cdot}e^{{i}t}`$. $`e^it`$ is $`f(t)`$. This means if $`t`$ is thought up as time $`f(t)`$ moves direction perpendicular to its position from the origin. </br>

[pic] </br>

When a circle, whose center is the origin. Then think about a moving point in a circle. We will find that the tangent to the circle is to the position from the origin. Since the tangent is the direction in which the point moves, you can induce that the function $`f(t)=e^{t{i}}`$ moves in a circle. </br>

[pic] </br>

Now we currently don’t know the radius of the circle in which $`e^{t{i}}`$ moves. However when $`t=0`$. The function becomes $`e^{0{i}}=e^0=1`$, Therefore the starting point of the function is 1. and the radius of the circle is 1. </br>

[pic] </br>

Now let us observe the speed in which this point moves. The speed in which the point moves is equal to the length of $`f'(t)={i}f(t)`$. We know that $`{i}f(x)`$ has the same length as $`f(x)`$. since $`f(x)`$ is in a unit circle its magnitude is $`1`$. Therefore the speed in which $`f(t)`$ moves is constantly $`1`$ and the total length $`f(t)`$ moves is $`t`$. </br>

[pic]  </br>

In conclusion the $`e^{t{i}}`$ is equal to a point on a unit circle with angle $`t`$ in the complex plane, which is $`cos{t}+{i}sin{t}`$.

## Quaternions:
If we look back at [the definition of imaginary numbers](#The-Definition-of-Imaginary-Numbers). We used the equation $`x^2=-1`$. Now Let’s suppose there are actually 3 numbers*(technically 6 since negative) that satisfies this equation $`i`$, $`j`$, $`k`$. these are also imaginary numbers. We will also define $`ijk=-1`$. These are what is used to define Quaternions. </br>

[pic]  </br>

Using these properties we can derive other equalities, such as 
- $`ij = k`$
- $`jk = i`$
- $`ki = j`$
  
- $`ji = -k`$
- $`kj = -i`$
- $`ik = -j`$

One thing to note unlike complex numbers quaternions _**will not**_ commute. commutativity only applies with imaginary and real numbers. When multiplying 2 different imaginary units, we can see that when the numbers are swapped the result will be negated. This property is called anti-commutivity.

## Quaternions Visualization:
Since quaternions are made up of 4 numbers we would have to use a 4d space to represent the number. Unfortunately we live in 3d space(spatial). Therefore it’s hard for us to wrap our heads around 4d space. Therefore instead of using 4d space, we will use 3d space, with each axis representing an imaginary part. I will call this the imaginary space for convenience. When the real part of the quaternions is needed we will just use the complex plane.

[pic]

## Quaternions as Rotations:

In the imaginary space, when multiplying $`k`$ to $`i`$ it becomes $`j`$. when multiplying $`j`$ to $`i`$ it becomes $`-k`$. We can see that both $`j`$ and $`k`$ are rotated 90 degrees with the axis of rotation being $`i`$. </br>

[pic] </br>

We can see the parallel with the complex numbers. using this fact Let's multiply $`e^{t{i}}`$ with $`q=a{j}+b{k}`$. if let $`f(t)=e^{t{i}}q`$. then $`f'(t)={i}f(t)`$, and so q is rotated t degrees around the $`i`$ axis!. </br>

[pic] </br>

With this we have successfully defined a rotation around the $`i`$ axis. </br>
Except… ****NO!**** watch what happens when $`i`$ is multiplied with $`e^{t{i}}`$ </br>

[gif] </br>

You can see that $`i`$ is shrinking and growing. What we want to happen is for $`i`$ to remain the same. Then how come that our function failed? If we look back at when $`e^{t{i}}`$ originaly did, we will remember that $`e^{t{i}}`$ rotated $`i`$ in the complex plane. Therefore $`i`$ shrinking was the consequence of this. 

[pic] </br>

One way to remedy this we can multiply $`e^{-t{i}}`$. This time we will multiply on the right side. By doing this we kept $`i`$, Then how will this new function affect $`j`$ and $`k`$? With the function $`f(t)=e^{t{i}}{\cdot}q{\cdot}e^{-t{i}}`$ we already know what $`e^{t{i}}`$ does, so we focus on $`q{\cdot}e^{-it}`$ and call it $`g(t)`$. If we differetiate $`q{\cdot}e^{-it}`$ we get $`q{\cdot}{(-i)}{\cdot}e^{-it}`$ if we assume $`q`$ is only composed of $`j`$ and $`k`$ then we know that we can swap $`(-i)`$ and $`q`$. and negate it. then the derivate becomes $`{i}{\cdot}q{\cdot}e^{-t{i}}={i}{\cdot}g(t)`$. We can see that this is also a rotation around the $`i`$ axis by $`t`$. This means the f(x) will rotate any quaternions about the $`i`$ axis by $`2t`$. Since we want to rotate by $`t`$ we can change the function to $`f(t)=e^{\frac{t{i}}{2}}{\cdot}q{\cdot}e^{-\frac{t{i}}{2}}`$.

## Generalization to any Axis:
Just like we did with $`i`$, multiplying by $`j`$ and $`k`$ lead to a 90 rotation around their repective axis. This mean we can generalize the function to work for all 3 axis. Now how could we generalize this to work for any axis? Let's say there are 2 vectors $`\vec{p}`$, $`\vec{q}`$ which is rotating once per second around a vector $`\vec{r}`$. now Let's say the velocity in which $`\vec{p}`$ and $`\vec{q}`$ is $`\vec{v_p}`$, $`\vec{v_q}`$. Now the velocity in which $`\vec{p} + \vec{q} `$ move's is equal to $`\vec{v_p} +\vec{v_q}`$.</br>

[pic]</br>

Now let's think of a different scenario. Have $`\vec{p}`$ be rotate around $`\vec{q}`$. let the velocity of $`\vec{p}`$ be $`\vec{v_p}`$. If we were to set $`\vec{q}`$ to be rotating around $`\vec{p}`$, we will find out that $`\vec{q}`$'s velocity is equal and opposite to $`\vec{v_p}`$ </br>

[pic] </br>

Using this fact we can say that if you want $`\vec{r}`$ rotate around a $`\vec{p} + \vec{q}`$, the velocity of $`\vec{r}`$ will be the sum of the velocity when rotating around $`\vec{p}`$, and the velocity when rotating around $`\vec{q}`$. In simple terms, you can deconstruct the velocity of a rotation into its basis components. </br>

[pic] </br>

So if I want to rotate a quaternion $`p`$ around a quaternion $`q=a{i}+b{j}+c{k}`$ with a length of 1. We would have $`e^{t\frac{a{i}+b{j}+c{j}}{2}}{\cdot}p{\cdot}e^{-t\frac{a{i}+b{j}+c{j}}{2}}`$ which is just $`e^{t\frac{q}{2}}{\cdot}p{\cdot}e^{-t\frac{q}{2}}`$.

## Computing $`\mathbf{e^{t{q}}}`$
We have used the notation $`e^{t{q}}`$ where q has a length of 1 and doesn't have a real part. However, we have never computed this value. so let’s think about how we would compute this value. When thinking about $`e^{t{i}}`$ we used a complex plane with the y axis being $`i`$. Now if we think of $`e^{t{q}}`$ with the y axis being $`q`$, you will find that $`1{\cdot}q=q`$, and $`q{\cdot}q=-1`$. Therefore we can use the same logic and say that $`e^{t{q}}`$ will be a point in a circle, however with the y axis being $`q`$. meaning $`e^{t{q}}=cos{t}+{q}sin{t}`$. </br>

[pic] </br>

## Conclusions
