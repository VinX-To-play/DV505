
let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python3.withPackages (python-pkgs: [
      python-pkgs.matplotlib
      ]))
  ];
  }

shellHook =
  ''
    git config user.email "cl224hx@student.lnu.se"
    git config user.name "Vincent Lundborg"
  '';