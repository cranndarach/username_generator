/*
 * usernames.js
 * Main script for the username generator.
 * Corpus is located in corpus.js, which is already loaded.
 */

function generateName() {
  let types = ["an", "aan", "aa", "adn", "vp", "dan", "aca", "va", "vpn", "npn", "nn", "vcv"];
  switch (_.sample(types)) {
    case "an":
      return makeName(adjective, noun);
    case "aan":
      return makeName(adjective, adjective, noun);
    case "aa":
      return makeName(adverb, adjective);
    case "adn":
      return makeName(adverb, determiner, noun);
    case "vp":
      return makeName(verb, preposition);
    case "dan":
      return makeName(determiner, adjective, noun);
    case "aca":
      return makeName(adjective, conjunction, adjective);
    case "va":
      return makeName(verb, adverb);
    case "vpn":
      return makeName(verb, preposition, noun);
    case "npn":
      return makeName(noun, preposition, noun);
    case "nn":
      return makeName(noun, noun);
    case "vcv":
      return makeName(verb, conjunction, verb);
  }
}

function makeName() {
  let cats = [...arguments];
  let picked = _.map(cats, _.sample);
  let cap = _.map(picked, _.capitalize);
  let username = _.join(picked, "");
  return username;
}

$(document).ready(() => {
  $("#content").append($("<button />", {
    id: "generateBtn",
    click: () => {
      $("#username").text = generateName();
    }
  }));
});
