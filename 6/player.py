#
# ばば抜きのプレイヤークラス。
#
require 'table'
require 'master'
require 'hand'
require 'card'


class Player

  # 進行役
  # @master
  # テーブル
  # @table
  # 自分の手札
  # @my_hand
  # 名前
  # @name

  #
  # コンストラクタ。
  # 
  def initialize(name, master, table, hand=Hand.new)
    @name = name
    @master = master
    @table = table
    @my_hand = hand
  end

  #
  # 順番を指名する。
  # 
  def play(next_player)
    # 次のプレイヤーに手札を出してもらう
    next_hand = next_player.show_hand

    # 相手の手札からカードを一枚引く
    picked_card = next_hand.pick_card

    # 引いた結果を表示
    print self, "：", next_player,"さんから ", picked_card,
    " を引きました\n"

    # 引いたカードを自分の手札に加え、同じ数のカードがあったら捨てる
    deal_card(picked_card)

    # 手札がゼロになったかどうか調べる
    if (@my_hand.get_number_of_cards == 0)
      # 進行役に上がりを宣言する
      @master.declare_win(self)
    else
      # 現在の手札を表示する
      print self, "：残りの手札は ", @my_hand, "です\n"
    end
  end


  #
  # 手札を見せる。
  # 
  def show_hand()
    # もしこの時点で手札が残り1枚ならば上がりとなるので宣言する
    if (@my_hand.get_number_of_cards == 1)
      @master.declare_win(self)
    end

    # 見せる前にシャッフルする
    @my_hand.shuffle()

    return @my_hand
  end

  #
  # カードを受け取る。
  # 
  def receive_card(card)
    # 引いたカードを自分の手札に加え、同じ数のカードがあったら捨てる
    deal_card(card)
  end

  #
  # プレイヤーの名前を返す。 <br>
  # Objectクラスのto_sメソッドをオーバーライドしたメソッド。
  # 
  def to_s
    return @name
  end


  private

  #
  # カードを自分の手札に加え、同じ数のカードがあったら捨てる。
  # 
  def deal_card(card)
    # カードを自分の手札に加える
    @my_hand.add_card(card)

    # 今加えたカードと同じカードを探す
    same_cards = @my_hand.find_same_number_card()

    # 同じカードの組み合わせが存在した場合
    if (same_cards != nil)
      # テーブルへカードを捨てる
      print self , "："
      @table.dispose_card(same_cards)
    end
  end

end
