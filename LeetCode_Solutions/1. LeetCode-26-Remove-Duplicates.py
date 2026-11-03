class Remove_Duplicates:
    def __init__(self,nums):
        self.nums = nums
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        for j in range(1, len(self.nums)):
            if self.nums[j] != self.nums[j-1]:
                self.nums[k] = self.nums[j]
                k += 1
        return k

def main():
    nums = [int(x) for x in input("Enter an array: ").split()]
    print(f"The Entire List: {nums}")
    rd = Remove_Duplicates(nums)
    k = rd.removeDuplicates(nums)

    print(f"Unique Elements Count: {k}")
    print(f"Array After Removing Duplicates: {nums[:k]}")

if __name__ == "__main__":
    main()
        