{
  description = "PyBambooHR: A Python wrapper for the BambooHR API";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
    in
    {
      packages = forAllSystems (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python311;
        in
        {
          default = python.pkgs.buildPythonPackage {
            pname = "PyBambooHR";
            version = "0.9.0";
            src = ./.;
            pyproject = true;

            build-system = [ python.pkgs.setuptools ];

            dependencies = with python.pkgs; [
              requests
              xmltodict
            ];

            nativeCheckInputs = with python.pkgs; [
              pytest
              httpretty
            ];

            checkPhase = ''
              runHook preCheck
              pytest tests/
              runHook postCheck
            '';

            meta = {
              description = "A Python wrapper for the BambooHR API";
              homepage = "https://github.com/philiptaron/PyBambooHR";
              license = pkgs.lib.licenses.mit;
            };
          };
        });

      devShells = forAllSystems (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          python = pkgs.python311;
        in
        {
          default = pkgs.mkShell {
            packages = [
              (python.withPackages (ps: with ps; [
                requests
                xmltodict
                pytest
                httpretty
              ]))
            ];
          };
        });

      checks = forAllSystems (system: {
        default = self.packages.${system}.default;
      });
    };
}
