# import pytest
# from game_of_greed.game_logic import *
# from game_of_greed.banker import *


# def test_roll_six():
#     roll = GameLogic.roll_dice(6)
#     assert len(roll) == 6
#     for value in roll:
#         assert 1 <= value <= 6

# def test_roll_five():
#     roll = GameLogic.roll_dice(5)
#     assert len(roll) == 5
#     for value in roll:
#         assert 1 <= value <= 6


# # Hey! test_roll_six and test_roll_five are REALLY similar
# # There's got to be a better way...

# @pytest.mark.parametrize(
#     "num_dice,expected_length",
#     [
#         (1,1),
#         (2,2),
#         (3,3),
#         (4,4),
#         (5,5),
#         (6,6),
#     ],
# )
# def test_all_valid_dice_rolls(num_dice, expected_length):
#     roll = GameLogic.roll_dice(num_dice)
#     assert len(roll) == expected_length
#     for value in roll:
#         assert 1 <= value <= 6



# # @pytest.mark.parametrize(
# #     "repetation_of_dice,expected_value",
# #     [
# #         ((0,0),0),
# #         ((1,1),100),
# #         ((1,6),4000),
# #         ((2,3),200),
# #         ((3,3),300),
# #         ((4,4),800),
# #         ((5,5),1500),
# #         ((5,6),2000),
# #         ((6,6),2400),
# #         (((6,6),(3,3),(4,5)),750),
# #         (((6,6),(3,3)),750),
# #         ((1,2,3,4,5,6),1500)


# #     ],
# # )
# # def test_all_valid_dice_rolls_score(repetation_of_dice, expected_value):
# #     roll = GameLogic.calculate_score(repetation_of_dice)
# #     assert roll == expected_value
   

# def test_shelf_unbanked():
#     actual=Banker()
#     actual.shelved=1000  
#     expected_ubbancked=1500
#     assert actual.shelf(500)==expected_ubbancked
#     assert actual.bank()==1500

# def test_clear_shelf():
#    actual=Banker()
#    actual.clear_shelf()
#    assert actual.shelved==0
#    assert actual.balance==0




