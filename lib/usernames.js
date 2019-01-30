/*
 * usernames.js
 * Main script for the username generator.
 * Corpus is located in corpus.js, which is already loaded.
 */

function generateName() {
  let types = ["an", "aan", "aa", "adn", "vp", "dan", "pdn", "aca", "va", "vpn", "npn", "nn", "vcv"];
  switch (_.sample(types)) {
    case "an":
      return makeName(adjectives, nouns);
    case "aan":
      return makeName(adjectives, adjectives, nouns);
    case "aa":
      return makeName(adverbs, adjectives);
    case "adn":
      return makeName(adverbs, determiners, nouns);
    case "vp":
      return makeName(verbs, prepositions);
    case "dan":
      return makeName(determiners, adjectives, nouns);
    case "pdn":
      return makeName(prepositions, determiners, nouns);
    case "aca":
      return makeName(adjectives, conjunctions, adjectives);
    case "va":
      return makeName(verbs, adverbs);
    case "vpn":
      return makeName(verbs, prepositions, nouns);
    case "npn":
      return makeName(nouns, prepositions, nouns);
    case "nn":
      return makeName(nouns, nouns);
    case "vcv":
      return makeName(verbs, conjunctions, verbs);
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
