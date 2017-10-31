require_relative './card.rb'
require 'byebug'

SUITS = ['SPADES', 'CLUBS', 'HEARTS', 'DIAMONDS']
VALUES = (1..9).to_a.map {|x| x.to_s} + ['J', 'K', 'Q', 'A']
class Board

  def initialize
    @grid = Array.new(4) {Array.new(13)}
    populate
    self.render
  end

  def populate
    cards = []
    SUITS.each do |s|
      VALUES.each do |v|
        cards << Card.new(s, v)
      end
    end

    cards.shuffle!

    @grid.each do |row|
      row.each_index do |col|
        row[col] = cards.pop
      end
    end
    return
  end

  def render
    @grid.each do |r|
      r.each do |c|
        print c.to_s
      end
      puts ' '
    end
  end

  def reveal(guessed_pos)
    
  end
end
