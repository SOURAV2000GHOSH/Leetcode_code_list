class Solution:
	def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

		properties = sorted(properties,key=lambda l:l[1], reverse=True)

		properties = sorted(properties,key=lambda l:l[0])

		result = 0

		length = len(properties)

		current_max_value = properties[length - 1][1]

		length = length - 2

		while length > -1:

			if properties[length][1] < current_max_value:
				result = result + 1

			else:
				current_max_value = properties[length][1]

			length = length - 1

		return result