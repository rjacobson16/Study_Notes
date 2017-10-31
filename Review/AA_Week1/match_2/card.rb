class Card
  attr_reader :value
  def initialize(suit, value)
    @suit = suit
    @value = value

    @face_up = false

  end

  def hide
    @face_up = false
  end

  def reveal
    @face_up = true
  end

  def to_s
    return "#{@value} of #{@suit}" if @face_up
    ' '
  end

  def ==(other_card)
    @value == other_card.value
  end
end
