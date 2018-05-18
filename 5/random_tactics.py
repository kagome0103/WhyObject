#
#==ランダムに手を決める戦略クラス。
#
require 'player'

class RandomTactics
  #
  # 戦略を読み、ジャンケンの手を得る。
  # グー・チョキ・パーのいずれかをPlayerクラスに定義された
  # 以下の定数で返す。
  # Player.STONE    ・・・ グー
  # Player.SCISSORS ・・・ チョキ
  # Player.PAPER    ・・・ パー
  # 
  def read_tactics
    # プレイヤーの手
    hand = 0

    # 0.0以上3.0未満の小数として乱数を得る
    random_num = rand()* 3.0
    if (random_num < 1.0)
      # randomNum が 0.0以上1.0未満の場合、グー
      hand = Player::STONE
    elsif (random_num < 2.0)
      # randomNum が 1.0以上2.0未満の場合、チョキ
      hand = Player::SCISSORS
    elsif (random_num < 3.0)
      # randomNum が 2.0以上3.0未満の場合、パー
      hand = Player::PAPER
    end

    # 決定した手を戻り値として返す
    return hand
  end
end

