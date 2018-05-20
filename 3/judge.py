#
#== ジャンケンの審判を表すクラス。
#
class Judge():
  #
  # ジャンケンを開始する。
  # 
  def start_janken(self, player1, player2):
    # ジャンケンの開始を宣言する
    print("【ジャンケン開始】")
    
    # ジャンケンを3回行う
    for cnt in range(0,3):
      # 何回戦目か表示する
      print("【" + str(cnt + 1) + "回戦目】")
      
      # プレイヤーの手を見て、どちらが勝ちかを判定する。
      winner = judge_janken(player1, player2) 
      
      if winner != None:
        # 勝者を表示する
        print(winner.get_name() + "が勝ちました!")
        
        # 勝ったプレイヤーへ結果を伝える
        winner.notify_result(true)
      else:
        # 引き分けの場合
        print("引き分けです！")
      
      # ジャンケンの終了を宣言する
      print("【ジャンケン終了】")
      
      # 最終的な勝者を判定する
      final_winner = judge_final_winner(player1, player2)
      
      # 結果の表示
      print( str(player1.get_win_count()) + " 対 " + str(player2.get_win_count()) + "で")
      
      if final_winner != None:
        print(final_winner.get_name() + "の勝ちです！")
      else:
        print("引き分けです！")

  #
  # 「ジャンケン、ポン！」と声をかけ、
  # プレイヤーの手を見て、どちらが勝ちかを判定する。
  # 
  def judge_janken(self, player1, player2):
    winner = None

    # プレイヤー１の手を出す
    player1hand = player1.show_hand()

    # プレイヤー２の手を出す
    player2hand = player2.show_hand()

    # それぞれの手を表示する
    print_hand(player1hand)
    print(" vs. ")
    print_hand(player2hand)

    # プレイヤー１が勝つ場合
    if (player1hand == Player::STONE and player2hand == Player::SCISSORS ) or \
       (player1hand == Player::SCISSORS and player2hand == Player::PAPER ) or \
       (player1hand == Player::PAPER and player2hand == Player::STONE):
      winner = player1
      # プレイヤー２が勝つ場合
    elif (player1hand == Player::STONE and player2hand == Player::PAPER ) or \
          (player1hand == Player::SCISSORS and player2hand == Player::STONE ) or \
          (player1hand == Player::PAPER and player2hand == Player::SCISSORS)
      winner = player2

    # どちらでもない場合は引き分け(nilを返す)
    return winner

  #
  # 最終的な勝者を判定する。
  # 
  def judge_final_winner(self, player1, player2):
    winner = None

    # Player1から勝ち数を聞く
    player1_win_count = player1.get_win_count()

    # Player2から勝ち数を聞く
    player2_win_count = player2.get_win_count()

    if player1_win_count > player2_win_count:
      # プレイヤー1の勝ち
      winner = player1
    elif player1_win_count < player2_win_count:
      # プレイヤー2の勝ち
      winner = player2

    # どちらでもない場合は引き分け(nilを返す)
    return winner

  #
  # ジャンケンの手を表示する。
  # 
  def print_hand(self, hand):
    if Player::STONE:
      print("グー")
    elif Player::SCISSORS:
      print("チョキ")
    elif Player::PAPER:
      print("パー")
