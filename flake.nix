{
  description = "Dayplanner";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachSystem [ "x86_64-linux" "aarch64-linux" ] (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
        fontsdotconf = (pkgs.makeFontsConf { fontDirectories = [
          pkgs.roboto
          pkgs.font-awesome
          pkgs.fira-code
        ];});
      in
      {
        packages.default = pkgs.stdenv.mkDerivation {
          name = "dayplanner";
          src = self;
          env = {
            FONTCONFIG_FILE = fontsdotconf;
          };
          buildPhase = "true";
          installPhase = "mkdir -p $out/app; install -t $out/app *.py";
          buildInputs = [
            (pkgs.python3.withPackages(ppkgs: [
              ppkgs.recurring-ical-events
              ppkgs.arrow
              ppkgs.icalendar
              ppkgs.pillow
              ppkgs.pyyaml
              ppkgs.requests
            ]))
          ];
        };
      });
}