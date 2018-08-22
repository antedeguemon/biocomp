s1 = "VLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLASVSTVLTSKY"
s2 = "VLSAADKTNVKAAWSKVGGHAGEYGAEALERMFLGFPTTKTYFPHFDLSHGSAQVKAHGKKVGDALTLAVGHLDDLPGALSNLSDLHAHKLRVDPVNFKLLSHCLLSTLAVHLPNDFTPAVHASLDKFLSSVSTVLTSKYR"


w = -4
def s(a,b)
  return 5 if a == b # match score
  -3 # mismatch score
end

s_matrix = (0..s1.length).map {(0..s2.length).map { |_| 0 }}
(0..s1.length).each { |i| s_matrix[i][0] = w * i }
(0..s2.length).each { |i| s_matrix[0][i] = w * i }

# it is naturally m+1 since it is inclusive
(1..s1.length).each do |i|
  (1..s2.length).each do |j|
    a = s_matrix[i-1][j-1] + s(s1[i-1], s2[j-1])
    b = s_matrix[i-1][j] + w
    c = s_matrix[i][j-1] + w
    s_matrix[i][j] = [a, b, c].max
  end
end

def distance(s, w)
  align1, align2 = s[0], s[1]
  score = (0..align1.length-1).map do |i|
    if align1[i] == align2[i] || (align1[i] != '-' && align2[i] != '-')
      s(align1[i], align2[i])
    else
      w
    end
  end.reduce(0, :+)
  identity = (0..align1.length-1).select do |i|
    align1[i] == align2[i]
  end.length

  [score, (identity.to_f / align1.length.to_f)]
end

def traceback(matrix, s1, s2, align1='', align2='', i=s1.length, j=s2.length)
  return [align1.reverse, align2.reverse] if (i <= 0 && j <= 0)
  if [i,j].min <= 0
    (i-1).downto(0).each { |k| align1 += s1[k]; align2 += '-' }
    (j-1).downto(0).each { |k| align2 += s2[k]; align1 += '-' }
    return [align1.reverse, align2.reverse]
  end

  cima, esquerda, diagonal = matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]
  if matrix[i][j] == diagonal + s(s1[i-1], s2[j-1])
    # diagonal
    traceback(matrix, s1, s2, align1+s1[i-1], align2+s2[j-1], i-1, j-1)
  elsif matrix[i][j] == esquerda + (-4)
    # esquerda yi alinhado com espaco
    traceback(matrix, s1, s2, align1+s1[i-1], align2+'-', i-1, j)
  elsif matrix[i][j] == cima + (-4)
    # cima -> xi alinhado com espaco
    traceback(matrix, s1, s2, align1+'-', align2+s2[j-1], i, j-1)
  end
end

print "Tabela final de alinhamento:\n"
(0..s1.length).each { |i|
  (0..s2.length).each { |j| print "#{s_matrix[i][j]}\t" }
  print "\n"
}
alinhadas = traceback(s_matrix, s1, s2)
print "\nCadeias alinhadas:\n#{alinhadas[0]}\n#{alinhadas[1]}\n"
print "\nDistancia: #{distance(alinhadas, w)}\n"
