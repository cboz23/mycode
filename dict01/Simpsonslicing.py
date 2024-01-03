#! /usr/bin/env python3

def main():

    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    
    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
    
    aword= challenge[2][1]
    bword= challenge[2][0]
    cword= challenge[3]

    print(f"My {aword}! The {bword} do {cword}!")

    dword= trial[2].get("goggles")
    eword= trial[2].get("eyes")
    fword= trial[3]

    print(f"My {dword}! The {eword} do {fword}!")

    a= nightmare[0]["user"]["name"]["first"]
    b= nightmare[0]["kumquat"]
    c= nightmare[0]["d"]

    print(f"My {a}! The {b} do {c}!")



main()




