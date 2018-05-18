#
# トランプのカードを表すクラス。
#
class Card
  # ジョーカーを表す定数
  JOKER        = 0
  # スペードを表す定数
  SUIT_SPADE   = 1
  # ダイヤを表す定数
  SUIT_DIAMOND = 2
  # クラブを表す定数
  SUIT_CLUB    = 3
  # ハートを表す定数
  SUIT_HEART   = 4
  
  # カードの示すスート
  # @suit
  # カードの示す数
  # @number
	
  #
  # コンストラクタ。
  # 
  def initialize(suit, number)
    @suit = suit
    @number = number
  end
	
  #
  # 数字を見る。
  # 
  attr_reader :number
	
  #
  # カードを文字列で表現する。
  # Objectクラスのto_sメソッドをオーバーライドしたメソッド。
  # 
  def to_s
    s = ""
    if (@number > 0)
      # スートの表示
      case @suit
      when SUIT_SPADE 
        s << "S"
      when SUIT_DIAMOND
        s << "D"
      when SUIT_CLUB
        s << "C"
      when SUIT_HEART
        s << "H"
      end
      # 数の表示
      case @number
      when 1
        s << "A"
      when 10
        s << "T"
      when 11
        s << "J"
      when 12
	s << "Q"
      when 13
	s << "K"
      else 
        s << @number.to_s
      end
    else
      # ジョーカーを表す
      s << "JK"
    end
		
    return s
  end
end
