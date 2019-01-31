/*
 * usernames.js
 * Main script for the username generator.
 * Corpus is located in corpus.js, which is already loaded.
 */

function generateName() {
  let types = ["an", "aan", "aa", "adn", "vp", "dan", "pdn", "aca", "va", "vpn", "npn", "nn", "vcv", "ncn"];
  switch (_.sample(types)) {
    case "an":
      console.log("adjective-noun");
      return makeName(adjectives, nouns);
    case "aan":
      console.log("adjective-adjective-noun");
      return makeName(adjectives, adjectives, nouns);
    case "aa":
      console.log("adverb-adjective");
      return makeName(adverbs, adjectives);
    case "adn":
      console.log("adverb-determiner-noun");
      return makeName(adverbs, determiners, nouns);
    case "vp":
      console.log("verb-preposition");
      return makeName(verbs, prepositions);
    case "dan":
      console.log("determiner-adjective-noun");
      return makeName(determiners, adjectives, nouns);
    case "pdn":
      console.log("preposition-determiner-noun");
      return makeName(prepositions, determiners, nouns);
    case "aca":
      console.log("adjective-conjunction-adjective");
      return makeName(adjectives, conjunctions, adjectives);
    case "va":
      console.log("verb-adverb");
      return makeName(verbs, adverbs);
    case "vpn":
      console.log("verb-preposition-noun");
      return makeName(verbs, prepositions, nouns);
    case "npn":
      console.log("noun-preposition-noun");
      return makeName(nouns, prepositions, nouns);
    case "nn":
      console.log("noun-noun");
      return makeName(nouns, nouns);
    case "vcv":
      console.log("verb-conjunction-verb");
      return makeName(verbs, conjunctions, verbs);
    case "ncn":
      console.log("noun-conjunction-noun");
      return makeName(nouns, conjunctions, nouns);
  }
}

function makeName() {
  let cats = [...arguments];
  let picked = _.map(cats, _.sample);
  let cap = _.map(picked, _.upperFirst);
  let username = _.join(cap, "");
  console.log(username);
  return username;
}

$(document).ready(() => {
  let $btn = $("<button />", {
    id: "generateBtn",
    class: "col s12 m6 offset-m3 l4 offset-l4 btn waves-effect waves-light",
    text: "Generate",
    click: () => {
      $("#username").text(generateName());
    }
  });
  let $row = $("<div />", {
    class: "row"
  });
  $row.append($btn);
  $("#content").append($row);
});
