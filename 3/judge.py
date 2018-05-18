#
#== ジャンケンの審判を表すクラス。
#
class Judge
  #
  # ジャンケンを開始する。
  # 
  def start_janken(player1, player2)
    # ジャンケンの開始を宣言する
    print "【ジャンケン開始】\n"
    
    # ジャンケンを3回行う
    for cnt in 0..3
      # 何回戦目か表示する
      print "【", (cnt + 1) , "回戦目】"
      
      # プレイヤーの手を見て、どちらが勝ちかを判定する。
      winner = judge_janken(player1, player2)
      
      if (winner != nil)
        # 勝者を表示する
        print "\n", winner.get_name(), "が勝ちました!\n"
        
        # 勝ったプレイヤーへ結果を伝える
        winner.notify_result(true)
      else
        # 引き分けの場合
        print "\n引き分けです！\n"
      end
      
      # ジャンケンの終了を宣言する
      print "【ジャンケン終了】\n"
      
      # 最終的な勝者を判定する
      final_winner = judge_final_winner(player1, player2)
      
      # 結果の表示
      print player1.get_win_count(), " 対 ", player2.get_win_count(), "で"
      
      if (final_winner != nil)
        print final_winner.get_name(), "の勝ちです！\n"
      else
        print "引き分けです！\n"
      end
    end
  end

  #
  # 「ジャンケン、ポン！」と声をかけ、
  # プレイヤーの手を見て、どちらが勝ちかを判定する。
  # 
  def judge_janken(player1, player2)
    winner = nil

    # プレイヤー１の手を出す
    player1hand = player1.show_hand()

    # プレイヤー２の手を出す
    player2hand = player2.show_hand()

    # それぞれの手を表示する
    print_hand(player1hand)
    print " vs. "
    print_hand(player2hand)
    print "\n"

    # プレイヤー１が勝つ場合
    if (player1hand == Player::STONE && player2hand == Player::SCISSORS ||
        player1hand == Player::SCISSORS && player2hand == Player::PAPER ||
        player1hand == Player::PAPER && player2hand == Player::STONE)
      winner = player1
      # プレイヤー２が勝つ場合
    elsif (player1hand == Player::STONE && player2hand == Player::PAPER ||
           player1hand == Player::SCISSORS && player2hand == Player::STONE ||
           player1hand == Player::PAPER && player2hand == Player::SCISSORS)
      winner = player2
    end

    # どちらでもない場合は引き分け(nilを返す)
    return winner
  end

  #
  # 最終的な勝者を判定する。
  # 
  def judge_final_winner(player1, player2)
    winner = nil

    # Player1から勝ち数を聞く
    player1_win_count = player1.get_win_count()

    # Player2から勝ち数を聞く
    player2_win_count = player2.get_win_count()

    if (player1_win_count > player2_win_count)
      # プレイヤー1の勝ち
      winner = player1
    elsif (player1_win_count < player2_win_count)
      # プレイヤー2の勝ち
      winner = player2
    end

    # どちらでもない場合は引き分け(nilを返す)
    return winner
  end

  #
  # ジャンケンの手を表示する。
  # 
  def print_hand(hand)
    case hand
    when Player::STONE
      print "グー"
    when Player::SCISSORS
      print "チョキ"
    when Player::PAPER
      print "パー"
    end
  end

end
