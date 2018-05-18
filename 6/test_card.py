#
# Card クラスのテスト
#
require 'test/unit'
require 'card'

class TestCard < Test::Unit::TestCase
  def setup
  end

  def teardown
  end

  def test_card1
    c = Card.new(Card::SUIT_SPADE, 3)
    assert_equal(3, c.number)
    assert_equal("S3", c.to_s)
  end

  def test_card2
    c = Card.new(Card::SUIT_DIAMOND, 1)
    assert_equal(1, c.number)
    assert_equal("DA", c.to_s)
  end

  def test_card3
    c = Card.new(Card::SUIT_CLUB, 10)
    assert_equal(10, c.number)
    assert_equal("CT", c.to_s)
  end

  def test_card4
    c = Card.new(Card::SUIT_HEART, 11)
    assert_equal(11, c.number)
    assert_equal("HJ", c.to_s)
  end

  def test_card5
    c = Card.new(Card::SUIT_HEART, 12)
    assert_equal(12, c.number)
    assert_equal("HQ", c.to_s)
  end

  def test_card6
    c = Card.new(Card::SUIT_HEART, 13)
    assert_equal(13, c.number)
    assert_equal("HK", c.to_s)
  end

  def test_card7
    c = Card.new(Card::JOKER, 0)
    assert_equal("JK", c.to_s)
  end


end
