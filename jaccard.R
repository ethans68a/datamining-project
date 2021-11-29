jaccard <- function(a, b) {
  intersection = length(intersect(a, b))
  union = length(a) + length(b) - intersection
  return (intersection/union)
}


vec1 = c(0,1,1,0,1)
vec2 = c(1,0,1,0,1)
jaccard(c(0,1,1,0,1),c(1,0,1,0,1))
cosine(vec1,vec2)
vec3 = c(1,1,1,1,1)
vec4 = c(1,1,1,1,1)
vec5 = c(0,0,0,1,1)
vec6 = c(1,1,1,0,0)
cosine(vec5,vec6)
cosine(rep(1,5),rep(1,5))
