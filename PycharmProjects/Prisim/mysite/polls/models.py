from django.db import models

# Create your models here.
"""
class Session_Table(models.Model):
    Pri_SID=models.AutoField # unique session Id
    time_stamp=models.DateTimeField()#session created at this time
    Pri_no_of_players= models.PositiveIntegerField()
    #uuid to be used as one parameter for  winners table so duplicate data is not pushed in DB
    Pri_Pid=models.ForeignKey(Player_Details,on_delete=models.CASCADE())  #FK PID->table Player_Details
    Pri_game_Id=models.ForeignKey(Simulation_Details,on_delete=models.CASCADE())
    def __str__(self):
        return self.time_stamp
    #class Meta:
      #  db_table="Session_Table"

"""


"""
class Player_Details(models.Model):
    PID=models.AutoField()
    Player_fname=models.CharField(max_length= 50)
    Player_Company=models.CharFeild(max_length=50)
    Player_email=models.EmailField()
    Player_passwd=models.CharField(max_length=10 , default=5)""" """Can be added in future
    player_type=models.CharField(max_length=10)
    #class Meta:
     #   db_table="Player_Details"

"""

"""
class Simulation_Details(models.Model):
    GID=models.AutoField
    game_Turn=models.PositiveIntegerField(default=0)
    game_type=models.CharField(default="Price_Simulation")
    game_PlayerId=models.ForeignKey(Session_Table,on_delete=models.CASCADE())
    class Meta:
        db_table="Simulation_Details"
"""


class Gamer(models.Model):
    #Gamergame_id=models.IntegerField
    game_Type=models.CharField(max_length=20) #
    Number_of_players=models.PositiveIntegerField(default=1)
    no_Of_Trucks=models.PositiveIntegerField(default=25)
    """
    Nth_turn=models.PositiveIntegerField(default=15)
    empty_Cost=models.BigIntegerField(default=400)
    loaded_Cost=models.BigIntegerField(default=550)
    unused_capital_cost=models.BigIntegerField(default=250)
    brokerage_Cost=models.BigIntegerField(default=1200)
    """
    def __str__(self):
        return self.game_Type




"""
class Winners(models.Model):
    player_id=models.ForeignKey
    sessn_Id=models.ForeignKey
    winner_Id=models.ForeignKey
    game_Id=models.ForeignKey
    player_rank=models.PositiveIntegerField

"""






