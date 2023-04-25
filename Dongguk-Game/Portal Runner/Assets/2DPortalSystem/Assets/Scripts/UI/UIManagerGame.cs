using UnityEngine;
using UnityEngine.UI;

public class UIManagerGame : MonoBehaviour
{
    [Header("Indicator type portal")]
    [SerializeField] private Image IndicatorPortalImg;
    [SerializeField] private Color Orange;
    [SerializeField] private Color Blue;

    public void ChengedTypePortal(string _typePortal) {
        if (_typePortal == "Orange")
            IndicatorPortalImg.color = Orange;
        else
            IndicatorPortalImg.color = Blue;
    }
}
