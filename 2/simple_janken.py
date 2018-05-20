#
#== オブジェクト指向を使用しないジャンケンプログラム
#

import random

# ジャンケンの手を表す定数
STONE = 0 # グー
SCISSORS = 1 # チョキ
PAPER = 2 # パー

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 　プログラムのスタートはここから
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

player1_win_count = 0 # プレイヤー１の勝ち数
player2_win_count = 0 # プレイヤー２の勝ち数
player1_hand = 0 # プレイヤー１が出す手
player2_hand = 0 # プレイヤー２が出す手

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
    random_num = random.randrange(0,2,1)

    if random_num == 0:
        player1_hand = STONE
        print("グー")
    elif random_num == 1:
        player1_hand = SCISSORS
        print("チョキ")
    elif random_num == 2:
        player1_hand = PAPER
        print("パー")

    print(" vs. ")

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■
    # 　(3) プレイヤー２が何を出すか決める
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■
    random_num = random.randrange(0,2,1)

    if random_num == 0:
        player2_hand = STONE
        print("グー")
    elif random_num == 1:
        player2_hand = SCISSORS
        print("チョキ")
    elif random_num == 2:
        player2_hand = PAPER
        print("パー")

    # ■■■■■■■■■■■■■■■■■■■■■■■■■■
    # 　(4) どちらが勝ちかを判定し、結果を表示する
    # ■■■■■■■■■■■■■■■■■■■■■■■■■■

    # プレイヤー１が勝つ場合
    if (player1_hand == STONE and player2_hand == SCISSORS) or \
       (player1_hand == SCISSORS and player2_hand == PAPER) or \
       (player1_hand == PAPER and player2_hand == STONE):
        print("\nプレイヤー１が勝ちました！\n")

        # ■■■■■■■■■■■■■■■■■■■■■■■■
        # 　(5) プレイヤー１の勝った回数を加算する
        # ■■■■■■■■■■■■■■■■■■■■■■■■
        player1_win_count += 1
    # プレイヤー２が勝つ場合
    elif (player1_hand == STONE and player2_hand == PAPER) or \
         (player1_hand == SCISSORS and player2_hand == STONE) or \
         (player1_hand == PAPER and player2_hand == SCISSORS):
        print("\nプレイヤー２が勝ちました！\n")

        # ■■■■■■■■■■■■■■■■■■■■■■■■
        # 　(5) プレイヤー２の勝った回数を加算する
        # ■■■■■■■■■■■■■■■■■■■■■■■■
        player2_win_count += 1

    # 引き分けの場合
    else:
        print("\n引き分けです！\n")

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 　(8) 最終的な勝者を判定し、画面に表示する
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■
print("【ジャンケン終了】\n")

# プレイヤー１の勝ち数が多い時
if player1_win_count > player2_win_count:
    # プレイヤー１の勝ちを表示する。
    print(str(player1_win_count) + "対" + str(player2_win_count) + "でプレイヤー１の勝ちです！\n")
    # プレイヤー２の勝ち数が多い時
elif player1_win_count < player2_win_count:
    # プレイヤー２の勝ちを表示する。
    print(str(player1_win_count) + "対" + str(player2_win_count) + "でプレイヤー２の勝ちです！\n")
    # プレイヤー１と２の勝ち数が同じ時
elif player1_win_count == player2_win_count:
    # 引き分けを表示する。
    print(str(player1_win_count) + "対" + str(player2_win_count) + "で引き分けです！\n")
