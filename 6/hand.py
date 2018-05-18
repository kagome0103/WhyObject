#
# ばば抜きの手札を表すクラス。
#/
class Hand

  # 手札にあるカードを保持するためのリスト
  # @hand

  #
  # コンストラクタ。
  # 
  def initialize()
    @hand = []
  end


  #
  # カードを加える。
  # 
  def add_card(card)
    # カードをリストの最後に追加する
    @hand << card
  end

  #
  # カードを引く。
  # 
  def pick_card
    picked_card = @hand.delete_at(0)
    return picked_card
  end

  #
  # シャッフルする。
  #
  def shuffle
    # 手札の枚数を取得
    number = @hand.size

    # カードをランダムに抜き取って最後に加える動作を繰り返す
    (number * 2).times {
      # ランダムな位置からカードを一枚抜き取る
      pos = Integer(rand() *  number)
      picked_card = @hand.delete_at(pos)

      # 抜き取ったカードを最後に加える
      @hand << picked_card
    }
  end


  #
  # 枚数を数える。
  # 
  def get_number_of_cards
    return @hand.size
  end


  #
  # 同じ数のカードを探し、配列で戻す
  # 同じ数のカードがない場合は nil を返します。
  # 
  def find_same_number_card
    
    number_of_cards = @hand.size
    same_cards = nil

    # 手札にカードが1枚もない場合は何もしない
    if (number_of_cards > 0)
        
      # 最後に追加されたカードを取得する
      last_index = number_of_cards - 1
      last_added_card = @hand[last_index]

      # 最後に追加されたカードの数字を取得する
      last_added_card_num = last_added_card.number

      for index in 0..last_index - 1 do
        card = @hand[index]
        if (card.number == last_added_card_num)
          
          # 最後に追加されたカードと同じカードが見つかった場合
          # 見つかった組み合わせをsameCardsに格納し、ループを抜ける
          same_cards = Array.new
          same_cards[0] = @hand.delete_at(last_index)
          same_cards[1] = @hand.delete_at(index)
          break
        end
          # 同じ数の組み合わせが見つからなかった場合、
          # same_cardsはnilのままとなる。
      end

      return same_cards
    end
  end

  #
  # 手札にあるカードを文字列で表現する。
  # Objectクラスのto_sメソッドをオーバーライドしたメソッド。
  # 
  def to_s
    s = ""
    @hand.each { |card| 
      s << card.to_s
      s << " "
    }            
    
    return s
  end
    
end
