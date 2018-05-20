#
#== ジャンケンのプレイヤーを表すクラス。
#
import random

class Player():
  # ジャンケンの手を表す定数
  STONE = 0 # グー
  SCISSORS = 1 # チョキ
  PAPER = 2 # パー

  #------------------------
  # プレイヤークラスの属性
  #------------------------

  # プレイヤーの名前 
  # @name
  # プレイヤーの勝った回数 
  # @win_count

  #------------------------
  # プレイヤークラスの操作
  #------------------------


  #
  # プレイヤークラスのコンストラクタ。
  #
  def __init__(self,name):
    self.name = name
    self.win_count = 0


  #
  # ジャンケンの手を出す。
  #
  def show_hand(self):
    hand = 0   # プレイヤーの手

    random_num = random.randrange(0,2,1)
    if random_num == 0:
      hand = STONE
    elif random_num == 1:
      hand = SCISSORS
    elif random_num == 2:
      hand = PAPER

    # 決定した手を戻り値として返す
    return hand

  #
  # 審判から勝敗を聞く。勝ったら、引数 result は true
  #
  def notify_result(self):
    if (result)
      # 勝った場合は勝ち数を加算する
      win_count += 1

  #
  # 自分の勝った回数を答える。
  #
  def get_win_count(self):
    return win_count

  #
  # 自分の名前を答える。
  # 
  def get_name(self):
    return name

  # get_win_count(), get_name() は attr_reader :win_count :name で良い
