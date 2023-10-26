#Create a component that displays chips, with the ability to specify the maximum number of displayed chips and the maximum text length in a chip.
#Introduction: Given a component called ChipList which accepts three parameters:
#chips: the array of chips (optional);
#maxChips: the maximum number of chips displayed (optional);
#maxTextLength: the maximum length of text in a chip (optional);
#write logic to display the component according to the requirements specified below.
#Requirements
#Display the array of chips (the chips parameter) passed to the component according to the following rules:
#The number of displayed chips should be controlled by the maxChips parameter.
#If the maximum number of chips to be displayed is exceeded, indicate the number of chips that are not shown in the aside element with data-testid="exceeding-text".
#The length of text in each chip should be controlled by the maxTextLength parameter.
#If the maximum length of text in a chip is exceeded, attach an ellipsis symbol (…) after the last allowed letter.
#If no parameters are passed or the chips array is empty, return an empty React Fragment.
#Handle the edge cases of:
#no data being passed to the component;
#an empty chips array;
#the chips, maxChips and maxTextLength parameters being provided in all possible configurations;
#the maxChips and maxTextLength parameters having values less than or equal to 0.
#Do not change the way the App and ChipList components are exported.
#ChipList is the component that will be tested against a set of Unit Tests. The App component is only used for simulating the behaviour in the Preview tab; it will be not used in the Unit Tests.
#Ensure that the chips are displayed in the same order as they appear in the chips property. Be sure to provide the correct index for each chip in the data-testid property.






chip_list = ['127383','18283','3728183','112','3718','19810']

def display_chips(chip_list, num_chip, max_chip):

    if not chip_list or num_chip <=0 or max_chip <=0:
        return None

    for index, item in enumerate(chip_list):

        if index < num_chip:
            if len(item) <= max_chip:
                print(item)
            else:
                print(f"{item[:max_chip]}...")





display_chips(chip_list, 3,3)