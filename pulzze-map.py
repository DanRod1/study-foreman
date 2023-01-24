https://realpython.com/python-map-function/
Skip to content
Product
Solutions
Open Source
Pricing
Search
Sign in
Sign up
JaredLGillespie
/
CodinGame
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
CodinGame/Python/hooch-clash.py /
@JaredLGillespie
JaredLGillespie Adding Hooch Clash
Latest commit 971d9af on Aug 31, 2019
 History
 1 contributor
48 lines (31 sloc)  1.21 KB

# https://www.codingame.com/training/easy/hooch-clash


import math


ERROR = 0.001


def volume(diameter):
    return (4 / 3) * math.pi * (diameter / 2)**3


def volume_equal(v1, v2):
    return v1 - ERROR <= v2 <= v1 + ERROR


def solution():
    orb_size_min, orb_size_max = map(int, input().split())
    glowing_size_1, glowing_size_2 = map(int, input().split())

    target_volume = volume(glowing_size_1) + volume(glowing_size_2)
    sparkling_size_1 = glowing_size_1
    sparkling_size_2 = glowing_size_2
    sparkling_difference = glowing_size_2 - glowing_size_1

    for o1 in range(orb_size_min, orb_size_max + 1):
        v1 = volume(o1)

        for o2 in range(o1, orb_size_max + 1):
            v2 = volume(o2)
            if volume_equal(v1 + v2, target_volume):
                if sparkling_size_1 == glowing_size_1 or o2 - o1 > sparkling_difference:
                    sparkling_size_1 = o1
                    sparkling_size_2 = o2
                    sparkling_difference = o2 - o1
                break

            if v1 + v2 > target_volume:
                break

    if sparkling_size_1 == glowing_size_1:
        print('VALID')
    else:
        print('{} {}'.format(sparkling_size_1, sparkling_size_2))


solution()
Footer
© 2023 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
