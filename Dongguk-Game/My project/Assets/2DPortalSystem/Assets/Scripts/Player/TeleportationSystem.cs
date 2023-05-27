using System;
using UnityEngine;

public class TeleportationSystem : MonoBehaviour
{
    [SerializeField] public float _radiusTrigerTeleport = 0.1f;
    [SerializeField] private float _maxSpeedTeleport = 20f;

    [HideInInspector] public Transform OrangeTeleport;
    [HideInInspector] public Transform BlueTeleport;

    public void Teleportation(GameObject _objTeleport, Rigidbody2D r2d)
    {
        if (_objTeleport.transform.position.x < OrangeTeleport.position.x + _radiusTrigerTeleport &&
            _objTeleport.transform.position.x > OrangeTeleport.position.x - _radiusTrigerTeleport &&
            _objTeleport.transform.position.y < OrangeTeleport.position.y + _radiusTrigerTeleport &&
            _objTeleport.transform.position.y > OrangeTeleport.position.y - _radiusTrigerTeleport)
        {
            TeleportingObject(OrangeTeleport.GetComponent<PortalDirection>(), BlueTeleport.GetComponent<PortalDirection>(), _objTeleport, r2d);
        }
        //Синий телепорт
        else if (_objTeleport.transform.position.x < BlueTeleport.position.x + _radiusTrigerTeleport &&
            _objTeleport.transform.position.x > BlueTeleport.position.x - _radiusTrigerTeleport &&
            _objTeleport.transform.position.y < BlueTeleport.position.y + _radiusTrigerTeleport &&
            _objTeleport.transform.position.y > BlueTeleport.position.y - _radiusTrigerTeleport)
        {
            TeleportingObject(BlueTeleport.GetComponent<PortalDirection>(), OrangeTeleport.GetComponent<PortalDirection>(), _objTeleport, r2d);
        }
    }

    private void TeleportingObject(PortalDirection _teleportOne, PortalDirection _teleportTwo, GameObject _objTeleport, Rigidbody2D r2d)
    {
        _objTeleport.transform.position = new Vector2(_teleportTwo.gameObject.transform.position.x - ((_radiusTrigerTeleport + 0.05f) * _teleportTwo.horizontalDirection),
                _teleportTwo.gameObject.transform.position.y - ((_radiusTrigerTeleport + 0.05f) * _teleportTwo.verticalDirection));
        //2 телепорта на одной горизонтальной поверхности
        if (_teleportOne.verticalDirection == _teleportTwo.verticalDirection && _teleportTwo.verticalDirection != 0)
        {
            r2d.velocity *= -1.02f;          
        }
        else
        //Телепорт 1 на горизонтальной, телепорт 2 - на вертикальной. Вход в телепорт 1
        if (Math.Abs(_teleportTwo.horizontalDirection) == Math.Abs(_teleportOne.verticalDirection) && _teleportOne.verticalDirection != 0)
        {
            _objTeleport.GetComponent<CharacterController>().multySpeed = -Math.Abs(r2d.velocity.y) / 2 * _teleportTwo.horizontalDirection;
        }
        else
        //Телепорт 1 на горизонтальной, телепорт 2 - на вертикальной. Вход в телепорт 2
        if (Math.Abs(_teleportOne.horizontalDirection) == Math.Abs(_teleportTwo.verticalDirection))
        {
            r2d.velocity = new Vector2(0, -Math.Abs(r2d.velocity.x) * _teleportTwo.verticalDirection * 1.7f);
        }
        //2 телепорта находятся на вертикальной поверхности
        else if (_teleportOne.horizontalDirection == _teleportTwo.horizontalDirection && _teleportTwo.horizontalDirection != 0)
        {
            _objTeleport.GetComponent<CharacterController>().multySpeed = -3 * _teleportTwo.horizontalDirection;
        }
        //Ограничение по скорости телепортации
        if (r2d.velocity.magnitude >= _maxSpeedTeleport)
        {
            r2d.velocity = new Vector2(r2d.velocity.y + (0.01f * _teleportOne.horizontalDirection), r2d.velocity.y + (0.5f * _teleportOne.verticalDirection));
        }
    }
}
