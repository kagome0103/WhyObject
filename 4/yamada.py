#
#==プレイヤーを継承した山田さんクラス。
#
require 'player'

class Yamada < Player
  #
  # コンストラクタ。
  #
  def initialize 
    super("山田さん")
  end

  #
  # ジャンケンの手を出す。
  # スーパークラスの同名メソッドをオーバーライドしている。
  #
  def show_hand
    # 必ずパーを出す
    return PAPER;
  end
end
