#
#==プレイヤーを継承した村田さんクラス。
#
require 'player'

class Murata < Player
  
  #
  # コンストラクタ。
  #
  def initialize 
    super("村田さん")
  end

  #
  # ジャンケンの手を出す。
  # スーパークラスの同名メソッドをオーバーライドしている。
  #
  def show_hand
    # 必ずグーを出す
    return STONE;
  end
end
