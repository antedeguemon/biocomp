s1 = "VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY"
s2 = "VLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHFDLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR"

w = -4
def s(a,b)
  return 5 if a == b # match
  -3 # mismatch
end

def distance(s, w)
  s1, s2 = s[0], s[1]
  score = (0..s1.length-1).map do |i|
    if s1[i] == s2[i] || (s1[i] != '-' && s2[i] != '-')
      s(s1[i], s2[i])
    else
      w
    end
  end.reduce(0, :+)
  identity = (0..s1.length-1).select do |i|
    s1[i] == s2[i]
  end.length

  [score, (identity.to_f / s1.length.to_f)]
end

def traceback(matrix, s1, s2, a1='', a2='', i=s1.length, j=s2.length)
  return [a1.reverse, a2.reverse] if (i <= 0 && j <= 0)
  if [i,j].min <= 0
    (i-1).downto(0).each { |k| a1 += s1[k]; a2 += '-' }
    (j-1).downto(0).each { |k| a2 += s2[k]; a1 += '-' }
    return [a1.reverse, a2.reverse]
  end

  cima, esquerda, diagonal = matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]
  if matrix[i][j] == diagonal + s(s1[i-1], s2[j-1])
    # diagonal
    traceback(matrix, s1, s2, a1+s1[i-1], a2+s2[j-1], i-1, j-1)
  elsif matrix[i][j] == esquerda + (-4)
    # esquerda yi alinhado com espaco
    traceback(matrix, s1, s2, a1+s1[i-1], a2+'-', i-1, j)
  elsif matrix[i][j] == cima + (-4)
    # cima -> xi alinhado com espaco
    traceback(matrix, s1, s2, a1+'-', a2+s2[j-1], i, j-1)
  end
end

s_matrix = (0..s1.length).map {(0..s2.length).map { |_| 0 }}
(0..s1.length).each { |i| s_matrix[i][0] = w * i }
(0..s2.length).each { |i| s_matrix[0][i] = w * i }

# n+1 porque intervalo fechado
(1..s1.length).each do |i|
  (1..s2.length).each do |j|
    a = s_matrix[i-1][j-1] + s(s1[i-1], s2[j-1])
    b = s_matrix[i-1][j] + w
    c = s_matrix[i][j-1] + w
    s_matrix[i][j] = [a, b, c].max
  end
end

print "Tabela final de alinhamento:\n"
(0..s1.length).each { |i|
  (0..s2.length).each { |j| print "#{s_matrix[i][j]}\t" }
  print "\n"
}
alinhadas = traceback(s_matrix, s1, s2)
print "\nCadeias alinhadas:\n#{alinhadas[0]}\n#{alinhadas[1]}\n"
d = distance(alinhadas, w)
print "\nIdentidade: #{d[0]}\nDistancia: #{d[1]}\n"
