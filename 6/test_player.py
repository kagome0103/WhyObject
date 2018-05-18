#
# Player クラスのテスト
#
require 'test/unit'
require 'player'
require 'table'
require 'master'
require 'hand'
require 'card'

#
# テスト用 Master クラス
#
class MasterMock < Master
  
  def initialize
    super()
    @win = false
  end

  def declare_win(winner)
    @win = true
    print winner, "さんが上がりました！\n"
  end
  def win?
    return @win
  end
end



#
# テスト用 Hand クラス
#
class HandMock < Hand
  # shuffle しても持手が換わらないようにする
  def shuffle
  end
end


class TestPlayer < Test::Unit::TestCase

  def setup
  end

  def teardown
  end

  def test_player
    table = Table.new
    # テスト用 Mock の作成
    master1 = MasterMock.new
    master2 = MasterMock.new
    hand1 = HandMock.new
    hand2 = HandMock.new
		
    # プレイヤー作成
    p1 = Player.new("P1", master1, table, hand1)
    p2 = Player.new("P2", master2, table, hand2)
		
    # 手札のチェック
    assert_equal("", hand1.to_s)
    p1.receive_card(Card::new(Card::SUIT_HEART, 2))
    p1.receive_card(Card::new(Card::SUIT_HEART, 3))
    assert_equal("H2 H3 ", hand1.to_s)
    assert_equal("H2 H3 ", p1.show_hand().to_s)
		
    # 同じカードを捨てる場合のチェック
    p1.receive_card(Card::new(Card::SUIT_HEART, 3))
    assert_equal("H2 ", hand1.to_s)
    assert_equal("H3 H3 ", table.to_s)
    assert_equal(false, master1.win?)
		
    # 隣の手札を引く
    p2.receive_card(Card::new(Card::SUIT_HEART, 4))
    p1.play(p2)
    assert_equal("H2 H4 ", hand1.to_s)
    assert_equal("H2 H4 ", p1.show_hand().to_s)

    # 同じカードを引く場合
    p2.receive_card(Card::new(Card::SUIT_HEART, 4))
    p1.play(p2)
    assert_equal("H2 ", hand1.to_s)
		
    # playの上がりチェック
    p2.receive_card(Card::new(Card::SUIT_HEART, 2))
    p2.receive_card(Card::new(Card::SUIT_HEART, 5))
    assert_equal(false, master1.win?)
    p1.play(p2)
    assert_equal("", hand1.to_s)
    assert_equal(true, master1.win?)

    # show_hand()上がりチェック
    master2 = MasterMock.new
    hand2 = Hand.new
    p2 = Player.new("P2", master2, table, hand2)
    p2.receive_card(Card::new(Card::SUIT_HEART, 5))		
    assert_equal(false, master2.win?)
    assert_equal("H5 ", p2.show_hand().to_s)
    assert_equal(true, master2.win?)
  end

end
