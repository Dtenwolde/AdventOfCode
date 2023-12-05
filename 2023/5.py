input_ = open("5_input.txt").read().split("\n\n")
#
# class Seed:
#     def __init__(self, seed):
#         self.seed = seed
#         self.soil = None
#         self.fertilizer = None
#         self.water = None
#         self.light = None
#         self.temp = None
#         self.hum = None
#         self.location = None
#
#     def __str__(self):
#         return f"({self.seed=}, {self.soil=}"
#         # return f"({self.seed=}, {self.soil=}, {self.fertilizer=}, " \
#         #        f"{self.water=}, {self.light=}, {self.temp=}, " \
#         #        f"{self.hum=}, {self.location=})"
#
#     __repr__ = __str__
#
# def map_converter(input_map, seed_list, from_attr, to_attr):
#     for map_ in input_map:
#         dest_start, source_start, length = map(int, map_.split())
#         print(dest_start, source_start, length)
#         for seed in seed_list:
#             from_ = getattr(seed, from_attr)
#             to_ = getattr(seed, to_attr)
#             for i in range(length):
#                 if from_ == source_start + i and to_ is None:
#                     setattr(seed, to_attr, dest_start + i)
#                     print(to_attr, from_, source_start, i, dest_start)
#     for seed in seed_list:
#         print(seed)
#         from_ = getattr(seed, from_attr)
#         to_ = getattr(seed, to_attr)
#         if to_ is None:
#             setattr(seed, to_attr, from_)
#             print(seed)
#
def main():
    seeds = input_[0].split(":")[-1].split()
    seed_list = []
    for idx in range(0, len(seeds), 2):
        seed_list.append((int(seeds[idx]), int(seeds[idx]) + int(seeds[idx + 1])))

    seed_soil = [list(map(int, ss.split())) for ss in input_[1].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, seed_soil)
    soil_fertilizer = [list(map(int, ss.split())) for ss in input_[2].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, soil_fertilizer)
    fertilizer_water = [list(map(int, ss.split())) for ss in input_[3].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, fertilizer_water)
    water_light = [list(map(int, ss.split())) for ss in input_[4].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, water_light)
    light_temp = [list(map(int, ss.split())) for ss in input_[5].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, light_temp)
    temp_hum = [list(map(int, ss.split())) for ss in input_[6].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, temp_hum)
    hum_location = [list(map(int, ss.split())) for ss in input_[7].split(":")[-1].strip().split("\n")]
    seed_list = map_p2(seed_list, hum_location)
    print(seed_list)
    min = seed_list[0][0]
    for seed, _ in seed_list[1:]:
        if seed < min:
            print(seed)
            min = seed
    print(min)
def map_p2(seed_list, map_list):

    append_list = []
    for soil_list in map_list:
        dst = soil_list[0]
        src = soil_list[1]
        range = soil_list[2]
        src_end = src + range
        next_seed_list = []
        while seed_list:
            start, end = seed_list.pop()
            before = (start, min(end, src))
            interval = (max(start, src), min(src_end, end))
            after = (max(src_end, start), end)
            if before[1] > before[0]:
                next_seed_list.append(before)
            if interval[1] > interval[0]:
                append_list.append((interval[0] - src + dst, interval[1] - src + dst))
            if after[1] > after[0]:
                next_seed_list.append(after)
        seed_list = next_seed_list
    return append_list + seed_list
            # if seed + interval < soil_start or seed > soil_end:
            #     # Will not have an intersection, so we can skip entire check
            #     print(f"Skip checks ({seed, interval} < {soil_start} or {seed} > {soil_end})")
            # elif seed < soil_start and seed + interval < soil_end:  # The start is less than the start of the interval
            #     diff = soil_start - seed
            #     next_seed_list.append((seed, diff))
            #     in_interval = seed + interval - soil_start
            #     next_seed_list.append((dest_start, in_interval))
            #     all_skipped = False
            # elif seed > soil_start and seed + interval <= soil_end:  # The range falls completely in the interval:
            #     diff_in_interval = seed - soil_start
            #     to_append = (dest_start + diff_in_interval, interval)
            #     next_seed_list.append(to_append)
            #     print(f"Completely in interval {to_append} {seed} {dest_start}")
            #     all_skipped = False
            # elif seed > soil_start and seed + interval > soil_end:
            #     diff_in_interval = soil_end - seed
            #     next_seed_list.append((dest_start + diff_in_interval, diff_in_interval))
            #     diff_out_interval = seed + interval - soil_end
            #     next_seed_list.append((soil_start + diff_out_interval, diff_out_interval))
            #     all_skipped = False
        # if all_skipped:
        #     next_seed_list.append((seed, interval))

if __name__ == "__main__":
    main()

# for seed, interval in seed_list:
#     for soil_list in seed_soil_list:
#         dest_start = soil_list[0]
#         soil_start = soil_list[1]
#         soil_range = soil_list[2]
#         soil_end = soil_start + soil_range
#         if seed + interval < soil_start or seed > soil_end:
#             # Will not have an intersection, so we can skip entire check
#             print(f"Skip checks ({seed, interval} < {soil_start} or {seed} > {soil_end})")
#             continue
#         elif seed < soil_start and seed + interval < soil_end: # The start is less than the start of the interval
#             diff = soil_start - seed
#             next_seed_list.append((seed, diff))
#             in_interval = seed + interval - soil_start
#             next_seed_list.append((dest_start, in_interval))
#         elif seed > soil_start and seed + interval <= soil_end: # The range falls completely in the interval:
#             diff_in_interval = seed - soil_start
#             to_append = (dest_start+diff_in_interval, interval)
#             next_seed_list.append(to_append)
#             print(f"Completely in interval {to_append} {seed} {dest_start}")
#         elif seed > soil_start and seed + interval > soil_end:
#             diff_in_interval = soil_end - seed
#             next_seed_list.append((dest_start+diff_in_interval, diff_in_interval))
#             diff_out_interval = seed + interval - soil_end
#             next_seed_list.append((soil_start + diff_out_interval, diff_out_interval))
# print(next_seed_list)
# [  )
    # soil_end
# If the intervals partly intersect, the part that intersects becomes a new list
# The part that does not intersect remains the old list with the same values
# The part that intersects becomes a new list with the new values (old value + some offset)
# This needs to be checked for both sides (smaller than and greater than)

# map_converter(seed_soil.split("\n"), seed_list, "seed", "soil")
# soil_fertilizer = input_[2].split(":")[-1].strip()
# map_converter(soil_fertilizer.split("\n"), seed_list, "soil", "fertilizer")
# fertilizer_water = input_[3].split(":")[-1].strip()
# map_converter(fertilizer_water.split("\n"), seed_list, "fertilizer", "water")
# water_light = input_[4].split(":")[-1].strip()
# map_converter(water_light.split("\n"), seed_list, "water", "light")
# light_temp = input_[5].split(":")[-1].strip()
# map_converter(light_temp.split("\n"), seed_list, "light", "temp")
# temp_hum = input_[6].split(":")[-1].strip()
# map_converter(temp_hum.split("\n"), seed_list, "temp", "hum")
# hum_location = input_[7].split(":")[-1].strip()
# map_converter(hum_location.split("\n"), seed_list, "hum", "location")
#
# min_location = seed_list[0].location
# for seed in seed_list[1:]:
#     if seed.location < min_location:
#         min_location = seed.location
#
# print(min_location)

