class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))

        # sort by position (closest to destination first)
        cars.sort(reverse=True)

        stack = []
        for pos, spd in cars:
            time = (target-pos)/spd

            # new fleet
            if not stack or time>stack[-1]:
                stack.append(time)

            # else join the fleet ahead
            # do nothing

        return len(stack)