#!/usr/bin/python

print("IEEE Workshop v1.0")
print("What's your name?")

name = input("My name is ")

print("Hello", name)

print("You want to calculate your passed and non-passed lessons?")

positiveAnswers = ['yes', 'y', 'yep']
negativeAnswers = ['no', 'n', 'nop']

answer = input()

if answer not in negativeAnswers and answer not in positiveAnswers:
    print("I don't understand, please run my again. Bye")
    quit()

if answer in negativeAnswers:
    print("OK, good bye...")
    quit()

print("OK, how many lessons you want to give me?")
lessons = int(input())

print("OK, i will remember it")

lessonRanks = []

for lessonIndex in range(lessons):
    print("Give me the rank for the lesson number " + str(lessonIndex + 1))
    lessonRanks.append(input())

for lessonIndex in range(lessons):
    print("Lesson No", lessonIndex + 1, "have rank =", lessonRanks[lessonIndex])
