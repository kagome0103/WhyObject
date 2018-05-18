#
# Table クラスのテスト
#
require 'test/unit'
require 'table'
require 'card'

class TestTable < Test::Unit::TestCase

  def setup
  end

  def teardown
  end

  def test_dispose_card
    t = Table.new   
    c = Array.new
    c[0] = Card.new(Card::SUIT_SPADE, 3)
    c[1] = Card.new(Card::SUIT_DIAMOND, 1)
    t.dispose_card(c)
    assert_equal("S3 DA ", t.to_s)

    c.clear
    c[0] = Card.new(Card::SUIT_HEART, 11)
    t.dispose_card(c)
    assert_equal("S3 DA HJ ", t.to_s)    
  end

end
