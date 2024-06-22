{ python311 }:
python311.pkgs.buildPythonPackage rec {
  pname = "callviz";
  version = "0.2.0";
  pyproject = true;

  src = ./.;

  nativeBuildInputs = with python311.pkgs; [
    setuptools
    wheel
  ];

  propagatedBuildInputs = with python311.pkgs; [
    graphviz
  ];

  pythonImportsCheck = [ "callviz" ];
}
