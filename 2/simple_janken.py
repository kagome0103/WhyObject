#
#== オブジェクト指向を使用しないジャンケンプログラム
#


# ジャンケンの手を表す定数
STONE = 0 # グー
SCISSORS = 1 # チョキ
PAPER = 2 # パー
	
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 　プログラムのスタートはここから
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

# プレイヤー１の勝ち数
player1_win_count = 0
		
# プレイヤー２の勝ち数
player2_win_count = 0

# プレイヤー１が出す手
player1_hand = 0
		
# プレイヤー２が出す手
player2_hand = 0

# ジャンケンの手を決めるのに使用する乱数
random_num = 0.0

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 　(1) プログラムが開始したことを表示する
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# プログラム開始メッセージを表示する
print("【ジャンケン開始】")

# ジャンケンを３回実施する
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 　(6) 勝負した回数を加算する
# 　(7) ３回勝負が終わったか？
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
for cnt in range(0,3):
  # 何回戦目かを表示する
  print("【" + str(cnt + 1) + "回戦目】")

  # ■■■■■■■■■■■■■■■■■■■■■■■■■■
  # 　(2) プレイヤー１が何を出すか決める
  # ■■■■■■■■■■■■■■■■■■■■■■■■■■
  # 0.0以上3.0未満の小数として乱数を得る
  random_num = rand() * 3.0

  if random_num < 1.0:
    # random_num が 0.0以上1.0未満 の場合、グー
    player1_hand= STONE

    # プレイヤー１の手を表示する
    print("グー")
  elif random_num < 2.0:
    # random_num が 1.0以上2.0未満 の場合、チョキ
    player1_hand= SCISSORS
    
    # プレイヤー１の手を表示する
    print("チョキ")
  elif random_num < 3.0:
    # random_num が 2.0以上3.0未満 の場合、パー
    player1_hand= PAPER
    
    # プレイヤー１の手を表示する
    print("パー")

  print(" vs. ")

  # ■■■■■■■■■■■■■■■■■■■■■■■■■■
  # 　(3) プレイヤー２が何を出すか決める
  # ■■■■■■■■■■■■■■■■■■■■■■■■■■
  
  # 0.0以上3.0未満の小数として乱数を得る
  random_num = rand() * 3.0

  if random_num < 1.0:
    # random_num が 0.0以上1.0未満 の場合、グー
    player2_hand= STONE
    
    # プレイヤー２の手を表示する
    print("グー")
  elif random_num < 2.0:
    # random_num が 1.0以上2.0未満 の場合、チョキ
    player2_hand= SCISSORS
    
    # プレイヤー２の手を表示する
    print("チョキ")
  elif random_num < 3.0:
    # random_num が 2.0以上3.0未満 の場合、パー
    player2_hand= PAPER
    # プレイヤー３の手を表示する
    print("パー")



  # ■■■■■■■■■■■■■■■■■■■■■■■■■■
  # 　(4) どちらが勝ちかを判定し、結果を表示する
  # ■■■■■■■■■■■■■■■■■■■■■■■■■■
  
  # プレイヤー１が勝つ場合
  if (player1_hand== STONE && player2_hand== SCISSORS ||
      player1_hand== SCISSORS && player2_hand== PAPER ||
      player1_hand== PAPER && player2_hand== STONE):
      # ジャンケンの結果を表示する
      print("\nプレイヤー１が勝ちました！\n")

    # ■■■■■■■■■■■■■■■■■■■■■■■■
    # 　(5) プレイヤー１の勝った回数を加算する
    # ■■■■■■■■■■■■■■■■■■■■■■■■
    player1_win_count += 1
  # プレイヤー２が勝つ場合
  elif (player1_hand== STONE && player2_hand== PAPER ||
         player1_hand== SCISSORS && player2_hand== STONE ||
         player1_hand== PAPER && player2_hand== SCISSORS):
    # ジャンケンの結果を表示する
    print("\nプレイヤー２が勝ちました！\n")

    # ■■■■■■■■■■■■■■■■■■■■■■■■
    # 　(5) プレイヤー２の勝った回数を加算する
    # ■■■■■■■■■■■■■■■■■■■■■■■■
    player2_win_count += 1
    
 # 引き分けの場合
  else:
    # ジャンケンの結果を表示する
    print("\n引き分けです！\n")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 　(8) 最終的な勝者を判定し、画面に表示する
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
print("【ジャンケン終了】\n")

# プレイヤー１の勝ち数が多い時
if player1_win_count > player2_win_count:
  # プレイヤー１の勝ちを表示する。
  print(player1_win_count + "対" + player2_win_count + "でプレイヤー１の勝ちです！\n")
  # プレイヤー２の勝ち数が多い時
elif player1_win_count < player2_win_count:
  # プレイヤー２の勝ちを表示する。
  print(player1_win_count + "対" + player2_win_count + "でプレイヤー２の勝ちです！\n")
  # プレイヤー１と２の勝ち数が同じ時
elif player1_win_count == player2_win_count:
  # 引き分けを表示する。
  print(player1_win_count + "対" + player2_win_count + "で引き分けです！\n")

