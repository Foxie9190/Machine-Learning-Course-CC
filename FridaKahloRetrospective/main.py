paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939,1933,1946,1940]
paintings = list(zip(paintings, dates))
paintings.append(("The Broken Column", 1944))
paintings.append(("The Wounded Deer", 1946))
paintings.append(("Me and My Doll", 1937))
#print(paintings) uncomment to see list of paintings with dates
len(paintings)
Audio_tour_number = list(range(1, 8))
#print(Audio_tour_number) Uncomment to see list of audio tour numbers
Master_list = list(zip(Audio_tour_number, paintings))
print(Master_list)
