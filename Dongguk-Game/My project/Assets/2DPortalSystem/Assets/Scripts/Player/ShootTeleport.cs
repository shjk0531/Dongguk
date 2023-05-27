using UnityEngine;

public class ShootTeleport : MonoBehaviour
{

    [SerializeField] private GameObject Bullet;

    [SerializeField] private PortalColor ShootType;

    private GameObject _activBullet;

    public enum PortalColor
    {
        Orange = 1,
        Blue = 2
    }

    private InputSystem Inputs;

    private void Awake()
    {
        Inputs = FindObjectOfType<InputSystem>();
        FindObjectOfType<UIManagerGame>().ChengedTypePortal(ShootType.ToString());
    }

    void Update()
    {

        if (!_activBullet)
        {
            if (Inputs.shootHorizontal != 0)
            {
                SpawnBullet(ShootType, Inputs.shootHorizontal, 0);
            }
            else if (Inputs.shootVertical != 0)
            {
                SpawnBullet(ShootType, 0, Inputs.shootVertical);
            }
           
        }

        if (Inputs.isWeaponChange)
        {
            if (ShootType == PortalColor.Orange)
            {
                ShootType = PortalColor.Blue;      
            }
            else
            {
                ShootType = PortalColor.Orange;
            }
            FindObjectOfType<UIManagerGame>().ChengedTypePortal(ShootType.ToString());
        }
    }

    private void SpawnBullet(PortalColor _tipeTeleport, float _directionX = 0, float _directionY = 0)
    {
        _activBullet = Instantiate(Bullet, transform.position, Quaternion.identity);
        Bullet _bullScr = _activBullet.GetComponent<Bullet>();
        _bullScr.verticalDirection = _directionY;
        _bullScr.horizontalDirection = _directionX;
        _bullScr.bulletType = (Bullet.PortalColor)_tipeTeleport;
    }
}
