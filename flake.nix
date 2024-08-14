{
  description = "A very basic flake";

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
        packages.default = pkgs.mkShell {
          name = "dayplanner";
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
          shellHook = ''
            export FONTCONFIG_FILE=${fontsdotconf}
          '';
        };
      });
}