# coding: utf-8
#require 'lingua/stemmer'
require 'socket'

class NewsController < ApplicationController

  HOSTNAME = "127.0.0.1"
  PORT = 8888
  
  def index
  end

  def search
    @query = params[:q]
    @results = []
    if @query
      s = TCPSocket.new HOSTNAME, PORT
      
      s.send @query + "\r\n", 0
      counter = 0
      while line = s.gets
	if counter == 50
	  break
	end
	@results.push(line.split("#"))
	counter = counter+1
      end
      s.close
    end
    # results = []
    # @query.split.each do |w|
    #   results.push(stemWord(w))
    # end    
    # if results
    #   wordList = array2quoted(results) # si es tamaño es 6, seleccionar solo los puntos
    #   qCategories = "SELECT categorias FROM palabras WHERE palabra IN (#{wordList})" # seleccionar id
    #   # del query comparar esas palabras con todas las que retorna qNews, calcular distancia, ordernar por distancia
    #   rs = ActiveRecord::Base.connection.exec_query(qCategories) # Retorna una lista de categorías
    #   catList = rsList(rs)
    #   qNews = "SELECT * FROM noticias WHERE categoria IN (#{catList}) LIMIT 10"
    #   @rsNews = ActiveRecord::Base.connection.exec_query(qNews)
    # end
  end

  @private
  def stemWord(word)
    stemmer = Lingua::Stemmer.new(:language => "es")
    rootWord = stemmer.stem(word)
    return rootWord
  end

  @private
  def rsList(rs)
    allCats = ""
    rs.each do |r|
      catLine = r["categorias"].gsub(/[0-9]/,'')
      allCats << catLine
    end
    categories = allCats.split.uniq
    return array2quoted(categories)
  end

  @private
  def array2quoted(arr)
    return arr.map{ |w| "'" + w + "'"}.join(",")
  end
  
end
