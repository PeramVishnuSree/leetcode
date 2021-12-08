#Given arr is an array of numbers and target is another array,
#Return True if arr can be manipulated into target by reversing any number of non-empty sub-arrays in arr.

for i in target:
            if i not in arr or target.count(i) != arr.count(i):
                return False
        return True