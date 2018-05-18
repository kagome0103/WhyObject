#
# テーブルを表すクラス。
#
class Table
  
  # 捨てられたカードを保持しておくためのリスト
  # @disposed_cards

  #
  # コンストラクタ。
  # 
  def initialize()
    @disposed_cards = []
  end

  #
  # カードを捨てる。
  # 
  def dispose_card(card)
    card.each {|c|
      # 捨てられたカードを表示する
      print c, " "
    }
    print "を捨てました\n"

    # 捨てられたカードはリストに追加して保持しておく。
    @disposed_cards.concat(card)
  end

  #
  # 捨てられたカードを文字列で表現する。
  # Objectクラスのto_sメソッドをオーバーライドしたメソッド。
  # 
  def to_s
    s = ""
    @disposed_cards.each {|card| 
      s << card.to_s
      s << " "
    }            
    
    return s
  end

end
